# Nanban - Friend
## Eye Blind Assist
A system that observes and describes a person's surrounding's to visually impaired people.

## v1
Version 1 is a simple basic prototype. 
It uses a object detection model to create a list of objects, a large language model frames a sentence with the list of objects. The sentence is then converted to speech.<br>
The object detection model used is efficientnet v2<br>
The large language model used is gpt-3.5<br>
Google text to speech is used to convert the text to speech.<br>
The computer used is a raspberry pi 4
<br>
<img align="up" src="Models/Screenshot A_2.png">

The program was split to 2 modes.
A) Live mode: A simple sentence is framed manually using the list of objects and rapidly told to the user.
Just simple concatinates the list of objects to a a prewritten sentence and reads it out. No language model is used.

B) Descriptive mode: A complex sentence is framed which can be easy to understand, and very well written sentence.
The data is send to gpt3.5 to create the complex sentence using the list of objects. 

### Additional features

Distance sensor is used to alert the user if he is going to collide onto an object. 

### Requirments 
#### Hardware
- Raspberry Pi - or other computers (tested on pi4)
- A Camera - usb or serial pi camera
- A Speaker - Any Earphones
- Distance Sensor - HC-SR04
- Switch
- Buzzer

##### Software
- Python(3.9) <br>
Once python is installed you can run the setup.sh file to install all files.<br>
`sudo ./setup.sh` <br>
<br>

Or you can manually install
- Tensorflow 
- Opencv
- OpenAI
- Espeak
- and dependencies of these programs
- You'll also have to install the efficientnet model
- (this will all be automatically done by the setup.sh file)

### Running 
- Assemble the circuit according the the circuit diagram.
  <img align="up" src="Circuit diagram.png">
- Connect the pi to its peripherals (or turn on the computer your using)
- Open the terminal and run
  `git clone https://github.com/mathew4STAR/EyeBlindAssist`
- Once installed cd into the folder
  `cd EyeBlindAssist`
- Run main.py
  `python3 main.py`
- In another terminal run the distance alert program
  `python3 ultrasonic.py`
- If you want to individually test systems cd into the tests folder and run the respective tests.

## v2
Same as v1 but more polished uses a efficientnet fine tuned object detection model. Large language model is switched to llama to run it locally on the computer. Ultrasonic is changed to Lidar to create a point cloud and get more data, and various other features.
```
----------------v2 has been discontinued, the project might resume later------------------------
```

## Additional information
The project was initially build in a few days for a hackathon.
Therefore there might be bugs,erros and lack of failsafes.
The projects code was initally sourced from tensorflow lite's examples. 

### Disclaimer
The project was made before Chatgpt(and other popular LLMs) became multimodal hence why the current approach.
