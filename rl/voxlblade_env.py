from rtgym import RealTimeGymInterface
from rl.voxlblade_agent import VoxlbladeAgent

class VoxlbladeEnv(RealTimeGymInterface):
    def __init__(self):
        self.agent = VoxlbladeAgent()
        pass
    def get_observation_space():
        pass
    def get_action_space():
        pass
    def get_default_action():
        pass
    def send_control():
        pass
    def reset():
        pass
    def get_obs_rew_terminated_info():
        pass
    def wait():
        pass
