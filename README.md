# deepracer

AWS DeepRacer Experimentation.

## Reward function

Definition from AWS

>The reward function describes immediate feedback (as a score for reward or penalty) when the vehicle takes an action to move from a given position on the track to a new position. Its purpose is to encourage the vehicle to make moves along the track to reach its destination quickly. The model training process will attempt to find a policy which maximizes the average total reward the vehicle experiences.

### Signature

```
def reward_function(params) :
    
    reward = ...

    return float(reward)
```

### Params

| Name                 | Description |
| :------------------- | :--------------|
| all_wheels_on_track  | (boolean) flag to indicate if the vehicle is on the track |
| x                    | (float) vehicle's x-coordinate in meters |
| y                    | (float) vehicle's y-coordinate in meters |
| distance_from_center | (float) distance in meters from the track center |
| is_left_of_center    | (boolean) flag to indicate if the vehicle is on the left side to the track center or not |
| heading              | (float) vehicle's yaw in degrees |
| progress             | (float) percentage of track completed |
| steps                | (int) numbers of steps completed |
| steering             | (float) -1 to 1 (-1 is right, 1 is left)                                            | speed                | (float) vehicle's speed in meters per second (m/s) |
| steering_angle       | (float) vehicle's steering angle in degrees |
| track_width          | (float) width of the track |
| waypoints            | [[float, float] … ] list of [x,y] as milestones along the track center |
| closest_waypoints    | [int, int] indices of the two nearest waypoints |


### Reward function

### Salamensa

A copy-and-paste from Amazon AWS of the sample reward function; used for learning purpose.

* [salamensa](./reward_functions/salamensa.py)

### Punisher

A first attempt to build an easiest reward function to train my model.

* [punisher](./reward_functions/punisher.py)


## Utils

Get last 10000 simulation jobs logs:

```bash
aws logs get-log-events --log-group-name "/aws/robomaker/SimulationJobs" --log-stream-name "<STREAM_NAME>" --output text --region us-east-1 > deepracer-sim.log
```
