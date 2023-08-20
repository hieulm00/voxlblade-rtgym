import pydirectinput
import cv2 as cv
import numpy as np
import cv as cv_utils

class VoxlbladeAgent():
    def send_control(self, walk_forward: bool):
        pydirectinput.keyDown('w') if walk_forward else pydirectinput.keyUp('w')
    def get_observation(self):
        screenshot = np.array(cv_utils.screenshot_window())
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        width = screenshot.shape[1]

        # HSV is clearer
        health_bar = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)
        # y-range, x-range
        health_bar = health_bar[59:67, (width - 181):(width - 86)]
        cv.imshow('Health Bar (HSV)', health_bar)
        # Mask for remaining health
        lower_range = (1, 1, 0)
        upper_range = (255, 255, 255)
        mask = cv.inRange(health_bar, lower_range, upper_range)
        health_bar_masked = cv.bitwise_and(health_bar, health_bar, mask=mask)
        # cv.imshow('Health Bar (Masked)', health_bar_masked)

        health = (np.count_nonzero(health_bar_masked[2]) * 100) / health_bar_masked[2].size

        print(health)
