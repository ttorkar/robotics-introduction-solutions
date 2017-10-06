
from robots.alice import Robot
from math import pi
import math as m

target_pos = (49.0235804,8.4316894)


def gps(pos):
    Lat_Distance = target_pos[1] - pos[1]
    Lon_Distance = target_pos[0] - pos[0]
    angle = m.atan2(Lat_Distance, Lon_Distance)
    print("Lat Distance: {}, Lon Distance: {}".format(Lat_Distance,Lon_Distance))
    print(angle)
    total_distance = Lat_Distance + Lon_Distance
    return angle, total_distance
        


def direction(angle_to_north, desired_direction):
    error = (angle_to_north) - desired_direction
    error %= 2*pi
    if error > pi:
        error -= 2*pi

    control = error * 3.0
    print("Error: ",error)
    print('Degrees:{}, Radians:{}'.format(int(control*180/pi),control))
    return control
    
def on_global_position(lat, lon, angle_to_north, accuracy):
    angle, total_distance = gps((lat, lon))
    robot.set_turn(direction(angle_to_north,angle))
    if total_distance == 0:
        robot.set_speed(0)  # Stop if at position
        print("At Desired Positon - Stopping")
        
robot = Robot()
robot.on_global_position = on_global_position
robot.set_speed(.1)  # move with 1 m/s

robot.wait()
robot.shutdown()
