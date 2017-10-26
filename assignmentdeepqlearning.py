from robots.alice import Robot
from math import pi
import random
import numpy as np
from collections import defaultdict

# Set up global variables
global data_bank, desired_direction, steps, X, y
data_bank = np.array([])

#Parameters
actions = [ 1,2,3,4] #Having out of index error with other values?
learning_rate = 0.01
discount_factor = 0.9
epsilon = 0.1
q_table = defaultdict(lambda: [0.0, 0.0, 0.0, 0.0, 0.0])

desired_direction = np.random.choice(actions)        

def __hash__(hash_value):
    return hash((hash_value))

# update q function with sample <s, a, r, s'>
def learn(prev_state, action, reward, current_state):
        current_q = q_table[prev_state][action]
        # using Bellman Optimality Equation to update q function
        new_q = reward + discount_factor * max(q_table[current_state])
        q_table[prev_state][action] += learning_rate * (new_q - current_q)
        
# get action for the state according to the q function table
# agent pick action of epsilon-greedy policy
def get_action(current_state):
    if np.random.rand() < epsilon:
        # take random action
        action = np.random.choice(actions)
        print('Random')
    else:
        # take action according to the q function table
        state_action = q_table[current_state]
        action = arg_max(state_action)
        print('Arg_Max')
    print(action)
    return action

def arg_max(state_action):
    max_index_list = []
    max_value = state_action[0]
    for index, value in enumerate(state_action):
        if value > max_value:
            max_index_list.clear()
            max_value = value
            max_index_list.append(index)
        elif value == max_value:
            max_index_list.append(index)
    return random.choice(max_index_list)

def direction(angle_to_north):
    error = (angle_to_north) - desired_direction
    error %= 2*pi
    if error > pi:
        error -= 2*pi

    control = error * 3.0
    return control

def on_global_position(lat, lon, angle_to_north, accuracy):
    robot.set_turn(direction(angle_to_north))

def process_sensor_data(sensor, data):
    global desired_direction, data_bank, count
    print(len(data_bank))
       
    if sensor == 'reward':
        data = data_bank[len(data_bank)-1][:-2].tolist()
        data.extend((desired_direction, -10))  # Add direction of travel and reward
        print('Episode finished')
    else:
        data.extend((desired_direction, 1))  # Add direction of travel and reward

    data = np.asarray(data)
    data = data.reshape(1,6)
    
    if len(data_bank) == 0:
        data_bank = data
    else:
        data_bank = np.concatenate((data_bank, data))
        
    #    If previous step exists, get action, previous_state and reward
        prev_state = data_bank[len(data_bank)-2][:4] #Get the previous state
        action = int(data_bank[len(data_bank)-2][4]) #Get the previous action
        reward = int(data_bank[len(data_bank)-2][5]) #Get the reward
        current_state = data_bank[len(data_bank)-1][:4] #Get the previous state
        
        
#        print('prev state', prev_state)
#        print('action', action)
#        print('reward', reward)
#        print('current state', current_state)
        
        if len(data_bank) % 100 == 0:
            #Convert to hash
            prev_state = __hash__(str(prev_state))
            current_state = __hash__(str(current_state))
    
            learn(prev_state, action, reward, current_state)
            
            action = get_action(str(current_state)) #Get new action
    
            desired_direction = action #Execute action
        
# Initialise Robot
robot = Robot()
robot.on_sensor_reading = process_sensor_data
robot.on_global_position = on_global_position
robot.set_speed(1)  # move with 1 m/s

robot.wait()
robot.shutdown()

