import gymnasium
from rl.voxlblade_env import VoxlbladeEnv

# player = VoxlbladeAgent()
# while True:
#     player.get_observation()
#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllWindows()
#         break
# print('Done.')

from rtgym import DEFAULT_CONFIG_DICT

conf = DEFAULT_CONFIG_DICT
conf['interface'] = VoxlbladeEnv

conf['time_step_duration'] = 0.05
conf['start_obs_capture'] = 0.05
conf['start_otime_step_timeout_factorbs_capture'] = 1
conf['ep_max_length'] = 100
conf['act_buf_len'] = 4
conf['reset_act_buf'] = False

env = gymnasium.make('real-time-gym-v1', config=conf)

obs, info = env.reset()

for _ in range(1):
    action = env.action_space.sample()
    obs, rew, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        obs, info = env.reset()

env.close()
