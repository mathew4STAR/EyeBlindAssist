from gpiozero import DistanceSensor
from gpiozero import Buzzer
from time import sleep

ultrasonic = DistanceSensor(echo=17, trigger=4)
buzzer = Buzzer(27)
buzzer.on()
sleep(2)
buzzer.off()


while True:
	print(ultrasonic.distance)
	if ultrasonic.distance  < 0.6:
		buzzer.on()
		#print("Stop you are close to an object")
	else:
		buzzer.off()
		#print("Safe to go")
