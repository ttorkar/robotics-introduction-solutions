from robots.alice import Robot
from time import sleep

robot = Robot()
while True:
    robot.set_led(0, True)
    sleep(0.5)
    robot.set_led(0, False)
    sleep(0.5)
