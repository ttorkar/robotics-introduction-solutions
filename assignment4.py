from robots.alice import Robot, ALICE_MAX_SPEED, ALICE_LEFT, ALICE_CENTER

robot = Robot(host="192.168.23.1")
robot.set_speed(ALICE_MAX_SPEED)


# Let's be smart this time...
def on_sensor_reading(sensor, data):
    if sensor == "distance/front":
        data = [2.0 if d <= 0.0 else d for d in data]
        #print(data)
        min_dist = min(data)
        if min_dist < 0.2:
            robot.set_turn(ALICE_LEFT)  # Use all speed to turn as sharp as possible
        else:
            robot.set_turn(ALICE_CENTER)  # No turn...


robot.on_sensor_reading = on_sensor_reading
robot.wait()
robot.shutdown()
