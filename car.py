import time
from gpiozero import Robot
robot = Robot(left=(7,8), right=(9,10))
robot.forward()
time.sleep(5)
robot.stop()
