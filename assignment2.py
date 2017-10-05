from robots.alice import Robot


robot = Robot()
led_state = [False, False, False, False]


def on_button_state_changed(button_id, state):
    if state:
        led_state[button_id] = not led_state[button_id]
        robot.set_led(button_id, led_state)


robot.on_button_state_changed = on_button_state_changed
robot.wait()
robot.shutdown()
