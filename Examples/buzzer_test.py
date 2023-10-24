from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(27)
buzzer.on()
time.sleep(5)
buzzer.off()
