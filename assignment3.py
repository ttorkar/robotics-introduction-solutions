from time import sleep
from robots.alice import Robot, ALICE_MAX_SPEED, ALICE_CENTER, ALICE_LEFT, ALICE_HALF_LEFT, ALICE_HALF_RIGHT, ALICE_RIGHT

sleep(3)

robot = Robot(host="192.168.23.1")
#robot = Robot()

LENGTH = 1.0
WIDTH = 0.5


def turn():
    robot.set_speed(ALICE_MAX_SPEED)
    robot.set_turn(ALICE_RIGHT)
    sleep(0.8)
    robot.set_turn(ALICE_CENTER)
    robot.set_speed(0.0)


def straight(dist):
    robot.set_speed(ALICE_MAX_SPEED)
    robot.set_turn(ALICE_CENTER)
    time = dist / ALICE_MAX_SPEED
    sleep(time)
    robot.set_speed(0)


straight(LENGTH)
turn()
straight(WIDTH)
turn()
straight(LENGTH)
turn()
straight(WIDTH)
turn()


robot.set_speed(0.0)
print("Done!")
sleep(3)

robot.shutdown()
