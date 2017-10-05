from time import sleep
from robots.alice import Robot, ALICE_MAX_SPEED, ALICE_CENTER, ALICE_LEFT, ALICE_HALF_LEFT, ALICE_HALF_RIGHT, ALICE_RIGHT

ALICE_HARDWARE = False
LENGTH = 1.0
WIDTH = 0.5

# Select if we need the hardware or not (localhost simulator).
robot = None
if ALICE_HARDWARE:
    robot = Robot(host="192.168.23.1")
else:
    robot = Robot()

def turn():
    robot.set_speed(ALICE_MAX_SPEED)
    robot.set_turn(ALICE_LEFT)
    # Value found empirically testing on the real alice robot
    # Whereas the simulation is calibrated correctly this also works in simulation.
    sleep(0.8)
    robot.set_turn(ALICE_CENTER)
    robot.set_speed(0.0)


def straight(dist):
    robot.set_speed(ALICE_MAX_SPEED)
    robot.set_turn(ALICE_CENTER)
    # Calculate the time we have to move to drive a certain distance.
    time = dist / ALICE_MAX_SPEED
    sleep(time)
    robot.set_speed(0.0)


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
