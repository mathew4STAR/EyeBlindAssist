from gpiozero import Button

button = Button(18)
print("True if its on on state and false if its on off state")
while True:
    print("The state of the switch is", button.is_pressed)