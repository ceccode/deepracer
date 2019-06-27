
def reward_function(params):

    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']

    SPEED_THRESHOLD = 2.0

    reward = 1e-3

    if all_wheels_on_track and speed > SPEED_THRESHOLD:
        reward = 1 * speed * progress

    return float(reward)
