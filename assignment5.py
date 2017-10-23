from robots.alice import Robot, MAX_SPEED, MAX_TURN
from math import pi
import time

desired_direction = -1.57
integrator = 0
last_time = None


def on_global_position(lat, lon, angle_to_north, accuracy):
    global desired_direction, integrator, last_time

    print("latlon: " + str(lat) + ":" + str(lon))

    dt = None
    if last_time is None:
        last_time = time.time()
        return
    else:
        dt = time.time() - last_time
        last_time = time.time()

    error = (-angle_to_north) - desired_direction
    error %= 2*pi
    if error > pi:
        error -= 2*pi

    print("ERR", error)

    integrator += error * dt

    p_gain = 3.0
    i_gain = 0.5

    control = error * p_gain# + integrator * i_gain

    robot.set_turn(-control * MAX_TURN)

    print("AN", angle_to_north)


robot = Robot()
robot.on_global_position = on_global_position
robot.set_speed(MAX_SPEED)  # move with 1 m/s

robot.wait()
robot.shutdown()
