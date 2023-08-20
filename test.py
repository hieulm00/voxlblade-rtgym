import cv2 as cv
from rl.voxlblade_agent import VoxlbladeAgent

player = VoxlbladeAgent()

while True:
    player.get_observation()
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
print('Done.')
