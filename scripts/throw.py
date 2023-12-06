from ur5py.ur5 import UR5Robot
import numpy as np
import time
import pdb

robot = UR5Robot(ip="192.168.131.69", gripper=2)
current_pose = np.array(robot.get_pose(convert=False))
end_pose = current_pose
end_pose[2] -= 0.01
poses = np.linspace(current_pose, end_pose, 20000)
pdb.set_trace()
for row in poses:
    pdb.set_trace()
    start_time = time.time()
    robot.servo_pose(row, time=0.02, convert=False)
    time.sleep(0.02)

def helper_sine(ini_start, ini_end, num):
    time = np.linspace(0, 1, num)
    speed = np.sin(np.pi * time)
    position = np.cumsum(speed)
    scaled_position = position - position[0]
    scaled_position = scaled_position / scaled_position[-1]
    scaled_position = ini_start + (ini_end - ini_start)*scaled_position
    #full_cycle_pos = np.concatenate((scaled_position, scaled_position[::-1]), axis=0)
    full_cycle_pos = scaled_position
    return full_cycle_pos

def helper_quintic(ini_start, ini_end, num):
    time = np.linspace(0, 1, num)
    trajectory = quintic(ini_start, ini_end, time)
    #positions = trajectory.y[:, 0]
    positions = trajectory.q
    #full_cycle_pos = np.concatenate((positions, positions[::-1]), axis=0)
    full_cycle_pos = positions
    return full_cycle_pos

def helper_trapezoidal(ini_start, ini_end, num):
    time = np.linspace(0, 1, num)
    trajectory = trapezoidal(ini_start, ini_end, time)
    #positions = trajectory.y[:, 0]
    positions = trajectory.q
    #full_cycle_pos = np.concatenate((positions, positions[::-1]), axis=0)
    full_cycle_pos = positions
    return full_cycle_pos
###### Helper end