from roblox_agent import RobloxAgent

player = RobloxAgent()

while True:
    player.send_control(walk_forward=True)
