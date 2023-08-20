import pydirectinput
import cv2 as cv
import numpy as np
import cv as cv_utils

class RobloxAgent():
    def send_control(self, walk_forward: bool):
        pydirectinput.keyDown('w') if walk_forward else pydirectinput.keyUp('w')
    def get_observation(self):
        screenshot = np.array(cv_utils.screenshot_window())
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        cv.imshow('VoxlBlade Gym', screenshot)
