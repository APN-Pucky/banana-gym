import gym
import gym_banana

from stable_baselines3 import PPO

env = gym.make("Banana-v0")

model = PPO("MlpPolicy", env, verbose=1)
#model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_banana_tensorboard/")
model.learn(total_timesteps=500000)