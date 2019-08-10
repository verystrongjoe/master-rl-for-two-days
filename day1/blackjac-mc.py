"""
https://github.com/LeanManager/Reinforcement_Learning/blob/master/Reinforcement%20Learning%20with%20Monte%20Carlo%20Methods.ipynb
"""

import gym
import sys
import numpy as np
from collections import defaultdict

from plot_util import plot_blackjack_values, plot_policy


env = gym.make('Blackjack-v0')

print('observation space : {}, action space : {}'.format(env.observation_space, env.action_space))


for i_episode in range(3):

    state = env.reset()

    while True:
        print(state)

        action = env.action_space.sample()

        print('Stick') if action == 0 else print('Hit')

        state, reward, done, info = env.step(action)

        if done:
            print('End game Reward : ' , reward)
            print('You won :)\n') if reward > 0 else print('You lose :\n')
            break


def generate_episode_from_limit_stochastic(bj_env):

    episode = []
    state = bj_env.reset()

    while True:
        probs = [0.8, 0.2] if state[0] > 18 else [0.2, 0.8]
        action = np.random.choice(np.arange(2), p=probs)
        next_state, reward, done, info = bj_env.step(action)
        episode.append((state, action, reward))
        state = next_state
        if done:
            break

    return episode

for i in range(3):
    print(generate_episode_from_limit_stochastic((env)))


def mc_prediction_q(env, num_episodes, generate_episodes, gamma=1.0):

    returns_sum = defaultdict(lambda: np.zeros(env.action_space.n))

    N = defaultdict(lambda : np.zeros(env.action_space.n))
    Q = defaultdict(lambda : np.zeros(env.action_space.n))

    for i_episode in range(1, num_episodes+1):

        if i_episode % 1000 == 0:
            print('\rEpisode {}/{}'.format(i_episode, num_episodes), end = '')
            sys.stdout.flush()

        episode = generate_episodes(env)

        states, actions, rewards = zip(*episode)

        discounts = np.array([gamma**i for i in range(len(rewards)+1)])

        for i, state in enumerate(states):

            returns_sum[state][actions[i]] += sum(rewards[i:]*discounts[:-(i+1)])

            N[state][actions[i]] += 1.0
            Q[state][actions[i]] = returns_sum[state][actions[i]] / N[state][actions[i]]

    return Q


Q = mc_prediction_q(env, 500000, generate_episode_from_limit_stochastic)

# obtain the corresponding state-value function
V_to_plot = dict((k,(k[0]>18)*(np.dot([0.8, 0.2],v)) + (k[0]<=18)*(np.dot([0.2, 0.8],v))) \
         for k, v in Q.items())

# k is the environment state
# v is the return for each of the two possible action in that state
plot_blackjack_values(V_to_plot)