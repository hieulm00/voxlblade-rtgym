import pygetwindow
import pyautogui

def screenshot_window():
    roblox = pygetwindow.getWindowsWithTitle('Roblox')[0]
    if roblox.title != 'Roblox':
        raise 'Window "Roblox" is not open!'
    roblox.activate()
    return pyautogui.screenshot(region=(roblox.left, roblox.top, roblox.width, roblox.height))
