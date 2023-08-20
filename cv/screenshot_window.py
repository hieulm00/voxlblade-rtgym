import pygetwindow
import pyautogui
from time import sleep

def screenshot_window():
    roblox = pygetwindow.getWindowsWithTitle('roblox')[0]
    roblox.activate()
    return pyautogui.screenshot(region=(roblox.left, roblox.top, roblox.width, roblox.height))
