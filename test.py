from rl.roblox_agent import RobloxAgent
import cv2 as cv

player = RobloxAgent()

# Recording the screen
while True:
    player.get_observation()
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
print('Done.')
