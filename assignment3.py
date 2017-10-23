from time import sleep
from robots.alice import Robot, MAX_SPEED, TURN_CENTER, TURN_LEFT, TURN_HALF_LEFT, TURN_HALF_RIGHT, TURN_RIGHT

ALICE_HARDWARE = True
LENGTH = 1.0
WIDTH = 0.5

# Select if we need the hardware or not (localhost simulator).
robot = None
if ALICE_HARDWARE:
    robot = Robot(host="eve-bot.local")
else:
    robot = Robot()

def turn():
    robot.set_speed(MAX_SPEED)
    robot.set_turn(TURN_LEFT)
    # Value found empirically testing on the real alice robot
    # Whereas the simulation is calibrated correctly this also works in simulation.
    sleep(0.8)
    robot.set_turn(TURN_CENTER)
    robot.set_speed(0.0)


def straight(dist):
    robot.set_speed(MAX_SPEED)
    robot.set_turn(TURN_CENTER)
    # Calculate the time we have to move to drive a certain distance.
    time = dist / MAX_SPEED
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
