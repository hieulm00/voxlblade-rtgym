import cv2 as cv
import numpy as np

def health_bar_exists(screenshot):
    width = screenshot.shape[1]
    detect_health_bar = screenshot[59:67, (width - 181):(width - 86)]
    detect_health_bar = cv.cvtColor(detect_health_bar, cv.COLOR_BGR2GRAY)
    detect_health_bar = cv.GaussianBlur(detect_health_bar, (3,3), 0)
    sobely = cv.Sobel(src=detect_health_bar, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
    # cv.imshow('Sobel Y', sobely)
    mean = np.mean(sobely)
    # print(mean)
    return mean > -133

def get_health_from_bar(screenshot):
    width = screenshot.shape[1]

    # HSV is clearer
    health_bar = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)
    # y-range, x-range
    health_bar = health_bar[59:67, (width - 181):(width - 86)]
    # cv.imshow('Health Bar (HSV)', health_bar)
    # Mask for remaining health
    lower_range = (1, 1, 0)
    upper_range = (255, 255, 255)
    mask = cv.inRange(health_bar, lower_range, upper_range)
    health_bar_masked = cv.bitwise_and(health_bar, health_bar, mask=mask)
    # cv.imshow('Health Bar (Masked)', health_bar_masked)

    return (np.count_nonzero(health_bar_masked[2]) * 100) / health_bar_masked[2].size
