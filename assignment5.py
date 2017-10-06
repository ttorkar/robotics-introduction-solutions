from robots.alice import Robot
from math import pi


#Radians
desired_direction = 1.57*3
integrator = 0
last_time = None

def direction(angle_to_north):
    error = (angle_to_north) - desired_direction
    error %= 2*pi
    if error > pi:
        error -= 2*pi

    control = error * 3.0
    print("Error: ",error)
    print('Degrees:{}, Radians:{}'.format(int(control*180/pi),control))
    return control
    
def on_global_position(lat, lon, angle_to_north, accuracy):
    robot.set_turn(direction(angle_to_north))
    

robot = Robot()
robot.on_global_position = on_global_position
robot.set_speed(0.1)  # move with 1 m/s

robot.wait()
robot.shutdown()
