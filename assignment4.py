from robots.alice import Robot, ALICE_MAX_SPEED, ALICE_LEFT, ALICE_CENTER

ALICE_HARDWARE = False

# Select if we need the hardware or not (localhost simulator).
robot = None
if ALICE_HARDWARE:
    robot = Robot(host="192.168.23.1")
else:
    robot = Robot()

robot.set_speed(ALICE_MAX_SPEED)


# Let's be smart this time...
def on_sensor_reading(sensor, data):
    if sensor == "distance/front":
        # When we see nothing 0.0 should be mapped to max distance of 2.
        data = [2.0 if d <= 0.0 else d for d in data]
        min_dist = min(data)

        # If there is something, just turn left
        if min_dist < 0.2:
            robot.set_turn(ALICE_LEFT)  # Use all speed to turn as sharp as possible
        else:
            robot.set_turn(ALICE_CENTER)  # No turn...


robot.on_sensor_reading = on_sensor_reading
robot.wait()
robot.shutdown()
