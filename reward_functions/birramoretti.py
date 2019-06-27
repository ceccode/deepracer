def reward_function(params):

    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    if not all_wheels_on_track:
        reward = 1e-3
    elif speed < 3:
        reward = 0.5
    else:
        reward = 1

    return float(reward)
