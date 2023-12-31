import numpy as np
from gymnasium import spaces
from rtgym import RealTimeGymInterface
from rl.voxlblade_agent import VoxlbladeAgent

class VoxlbladeEnv(RealTimeGymInterface):
    def __init__(self):
        self.agent = None
        self.initialized = False

    def get_observation_space(self):
        health_space = spaces.Box(low=0.0, high=100.0)
        return spaces.Tuple((health_space,))
    
    def get_action_space(self):
        return spaces.Box(low=np.array([0]), high=np.array([1]))
    
    def get_default_action(self):
        return np.array([0, 0])
    
    def send_control(self, control):
        self.agent.send_control(walk_forward=control[0])

    def reset(self, seed, options):
        if not self.initialized:
            self.agent = VoxlbladeAgent()
            self.initialized = True
        health = self.agent.get_observation()

        return [np.array([health], dtype=np.float32)], {}

    def get_obs_rew_terminated_info(self):
        health = self.agent.get_observation()
        obs = [np.array([health], dtype=np.float32)]
        rew = health
        terminated = health == 0.0
        info = {}
        return obs, rew, terminated, info

    def wait(self):
        self.send_control([0, 0])
