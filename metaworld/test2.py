import gym
gym.logger.set_level(40)

import metaworld
import random


print(metaworld.ML1.ENV_NAMES)  # Check out the available environments

SEED = 0  # some seed number here
ml1 = metaworld.ML1('pick-place-v2',seed=SEED) # Construct the benchmark, sampling tasks

env = ml1.train_classes['pick-place-v2']()  # Create an environment with task `pick_place`
task = random.choice(ml1.train_tasks)
env.set_task(task)  # Set task

obs = env.reset()  # Reset environment
a = env.action_space.sample()  # Sample an action
obs, reward, done, info = env.step(a)  # Step the environoment with the sampled random action
env.rend