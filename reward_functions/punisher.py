def reward_function(params):

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    ROADWAY = 0.50 * track_width
    CENTERWAY = 0.25 * track_width

    reward = 1

    # Reward if no wheels go off the track
    distance_from_border = ROADWAY - distance_from_center
    if all_wheels_on_track and distance_from_border >= 0.15:
        reward *= 1 * speed

    # Punish if outside track center
    if distance_from_center > 0.0 and distance_from_center > CENTERWAY:
        reward *= 1 - (distance_from_center / ROADWAY)

    # Punish if not all_wheels_on_track
    if not all_wheels_on_track:
        reward = 1e-3

    # Punish if the car is steering way too much
    ABS_STEERING_THRESHOLD = 0.5
    if abs(steering) > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)
