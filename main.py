from gpiozero import Buzzer
from gpiozero import Button
import argparse
import sys
import time
import os
import openai
openai.api_key = "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"
from espeak import espeak
import openai
import os
import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision

buzzer = Buzzer(27)
button = Button(18)
buzzer.on()
time.sleep(0.5)
buzzer.off()
time.sleep(0.2)
buzzer.on()
time.sleep(0.5)
buzzer.off()


def run(model: str, camera_id: int, width: int, height: int, num_threads: int,
        enable_edgetpu: bool) -> None:
  """Continuously run inference on images acquired from the camera.

  Args:
    model: Name of the TFLite object detection model.
    camera_id: The camera id to be passed to OpenCV.
    width: The width of the frame captured from the camera.
    height: The height of the frame captured from the camera.
    num_threads: The number of CPU threads to run the model.
    enable_edgetpu: True/False whether the model is a EdgeTPU model.
  """

  # Variables to calculate FPS
  counter, fps = 0, 0
  start_time = time.time()
  nonet = False
  # Start capturing video input from the camera
  cap = cv2.VideoCapture(camera_id)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

  # Visualization parameters
  row_size = 20  # pixels
  left_margin = 24  # pixels
  text_color = (0, 0, 255)  # red
  font_size = 1
  font_thickness = 1
  fps_avg_frame_count = 10

  # Initialize the object detection model
  base_options = core.BaseOptions(
      file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)
  detection_options = processor.DetectionOptions(
      max_results=3, score_threshold=0.3)
  options = vision.ObjectDetectorOptions(
      base_options=base_options, detection_options=detection_options)
  detector = vision.ObjectDetector.create_from_options(options)
  # Continuously capture images from the camera and run inference
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      sys.exit(
          'ERROR: Unable to read from webcam. Please verify your webcam settings.'
      )

    counter += 1
    image = cv2.flip(image, 1)

    # Convert the image from BGR to RGB as required by the TFLite model.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a TensorImage object from the RGB image.
    input_tensor = vision.TensorImage.create_from_array(rgb_image)
    if button.is_pressed:
      mode = "d"
    else:
      mode = "l"
    if nonet == True:
      mode = "l"
    # Run object detection estimation using the model.
    if mode == "l":
      detection_result = detector.detect(input_tensor)
      step = 50
      if True:
        lis = []
        for detection in detection_result.detections:
          category = detection.categories[0]
          name = category.category_name
          lis.append(name)
        #espeak.synth("There is a")
        val = "There is a "
        for i in range(len(lis)):
          if i == (len(lis) - 1):
            #espeak.synth("and")
            val += " and "
          #espeak.synth(lis[i])
          val += lis[i] + ", "
        print(lis)
        print(val)
        try:
          os.system(f"./speech.sh “{val}”")
        except:
          espeak.say(val)
        print("------")
    if mode == "d":
      detection_result = detector.detect(input_tensor)
      if True:
        lis = []
        for detection in detection_result.detections:
          category = detection.categories[0]
          name = category.category_name
          lis.append(name)
        prompt = "Your helping a blind person there is a "
        for i in range(len(lis)):
          if i == (len(lis) - 1):
            prompt += lis[i] + ","
        prompt += "in front of him. Explain that to him in 10 words"
        print(prompt)
        try:
          completion = openai.ChatCompletion.create(model="gpt-3.5-turbo" ,messages=[{"role": "user", "content": prompt}])
          print(completion.choices[0].message.content)
          os.system(f"./speech.sh “{completion.choices[0].message.content}”")
        except:
          print("No net")
          buzzer.on()
          time.sleep(1)
          buzzer.off()
          time.sleep(0.5)
          buzzer.on()
          time.sleep(1)
          buzzer.off()
          time.sleep(0.5)
          buzzer.on()
          time.sleep(1)
          buzzer.off()
          nonet = True
    # Draw keypoints and edges on input image
    #unwanted- image = utils.visualize(image, detection_result)
    # Calculate the FPS
    if counter % fps_avg_frame_count == 0:
      end_time = time.time()
      fps = fps_avg_frame_count / (end_time - start_time)
      start_time = time.time()

    # Show the FPS
    fps_text = 'FPS = {:.1f}'.format(fps)
    text_location = (left_margin, row_size)
    #unwanted- cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
    #            font_size, text_color, font_thickness)

    # Stop the program if the ESC key is pressed.
    if cv2.waitKey(1) == 27:
      break
    #cv2.imshow('object_detector', image)

  cap.release()
  cv2.destroyAllWindows()



def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Path of the object detection model.',
      required=False,
      default='efficientdet_lite0.tflite')
  parser.add_argument(
      '--cameraId', help='Id of camera.', required=False, type=int, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of frame to capture from camera.',
      required=False,
      type=int,
      default=640)
  parser.add_argument(
      '--frameHeight',
      help='Height of frame to capture from camera.',
      required=False,
      type=int,
      default=480)
  parser.add_argument(
      '--numThreads',
      help='Number of CPU threads to run the model.',
      required=False,
      type=int,
      default=4)
  parser.add_argument(
      '--enableEdgeTPU',
      help='Whether to run the model on EdgeTPU.',
      action='store_true',
      required=False,
      default=False)
  args = parser.parse_args()

  run(args.model, int(args.cameraId), args.frameWidth, args.frameHeight,
      int(args.numThreads), bool(args.enableEdgeTPU))


if __name__ == '__main__':
  main()
