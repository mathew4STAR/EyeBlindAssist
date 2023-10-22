# Nanban - Friend
## Eye Blind Assist
A system that observes and describes a person's surrounding's to visually impaired people. 

## v1
Version 1 is a simple basic prototype.
It uses a object detection model to create a list of objects, a large language model frames a sentence with the list of objects. The sentence is then converted to speech.
The object detection model used is efficientnet v2
The large language model used is gpt-3.5
Google text to speech is used to convert the text to speech.
The computer used is a raspberry pi 4

The program was split to 2 modes.
A) Live mode: A simple sentence is framed manually using the list of objects and rapidly told to the user.
Just simple concatinates the list of objects to a a prewritten sentence and reads it out. No language model is used.

B) Descriptive mode: A complex sentence is framed which can be easy to understand, and very well written sentence, like a poem.
The data is send to gpt3.5 to create the complex sentence using the list of objects. 

### Additional features

Distance sensor is used to alert the user if he is going to collide onto an object. 

### Requirments 
#### Hardware
- Raspberry Pi - or other amr based computers
- A Camera - usb or serial pi camera
- A Speaker - Any Earphones
- Distance Sensor - HC-SR04
- Switch
- Buzzer

##### Software
- Python 3.6 
Once python is installed you can run the requirments.txt file to install all files.<br>
Or you can manually install
- Tensorflow 
- Opencv
- Espeak

## v2
Same as v1 but more polished uses a efficientnet fine tuned object detection model. Large language model is switched to alpace to run it locally on the computer. Ultrasonic is changed to Lidar to create a point cloud and get more data, and various other features.
```
----------------v2 has been discontinued, the project might resume later------------------------
```

## Additional information
The project was initially build in a few days for a hackathon.
Therefore there might be bugs,erros and lack of failsafes.
The projects code was initally sourced from tensorflow lite's examples. 
