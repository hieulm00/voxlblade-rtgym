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

        width = screenshot.shape[1]
        
        # y-range, x-range
        health_bar = screenshot[55:70, (width - 190):(width - 80)]
        cv.imshow('Health Bar', health_bar)
