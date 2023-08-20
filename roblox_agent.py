import pydirectinput

class RobloxAgent():
    def send_control(self, walk_forward: bool):
        pydirectinput.keyDown('w') if walk_forward else pydirectinput.keyUp('w')
        pass
    def get_observation():
        # TODO!
        pass
