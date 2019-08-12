import tensorflow as tf
import tensorflow.keras.layers as kl
from tensorflow.keras.models import Model
from tensorflow.python.keras.optimizers import Adam

import gym
from collections import deque
import numpy as np
import random

"""
Hyperparameters
"""
minibatch_size = 64
replay_memory_size = 2000
agent_history_length = 4
target_network_update_frequency = 10000
discount_factor = 0.99
action_repeat = 4
learning_rate = 0.001
initial_exploration = 1.
final_exploration = 0.01
final_exploration_frame = 100000
replay_start_size = 50000  # warm up before count of samples in memory becomes replay_start_size, it use ramdom poilcy.
no_op_max = 30   # every episode it doesn't do any action until no_op_max pasts.

# update_frequency = 4  # what is it?!
# gradient_momentum = 0.95  # RMSProp
# squared_gradeint_momentum = 0.95  # RMSProp
# min_squared_gradeint = 0.01   # RMSProp

"""
Agent
"""
class Agent:
    def __init__(self, state_size, action_size):
        self.replay_memory = deque([], maxlen=replay_memory_size)
        # self.model = model
        self.n_steps = 0
        self.n_epsiodes = 0
        self.epsilon = initial_exploration
        self.epsilon_decay = (initial_exploration - final_exploration) / final_exploration_frame
        self.epsilon_decay = 0.999
        self.state_size = state_size
        self.action_size = action_size
        self.discounted_factor = discount_factor

        # https://www.tensorflow.org/versions/r2.0/api_docs/python/tf/keras/models/clone_model
        # self.target_model = tf.keras.models.clone_model(self.model)
        # self.target_model = DeepQNetwork(state_size=state_size, action_size=action_size)

        self.model= build_network(state_size, action_size)
        self.target_model = build_network(state_size, action_size)
        self.update_target()


    def update_target(self):
        self.target_model.set_weights(self.model.get_weights())

    def reset(self):
        self.replay_memory.clear()

    def select_action(self, state):
        if np.random.rand() <= self.epsilon:
            # return np.random.choice(self.action_size, 1)[0]
            return random.randrange(self.action_size)

        else:
            value = self.model.predict(np.expand_dims(s, axis=0))[0]
            return np.argmax(value)

    def append_sample(self, state, action, reward, next_state, done):
        self.replay_memory.append(([state, action, reward, next_state, done]))
        if self.epsilon > final_exploration:
            self.epsilon *= self.epsilon_decay

    def sample(self, minibatch_size):
        return random.sample(self.replay_memory, minibatch_size)

    def train(self):
        # if len(self.replay_memory) < replay_start_size:
        #     return
        if len(self.replay_memory) < minibatch_size:
            return

        samples = self.sample(minibatch_size)

        states = []
        actions = []
        rewards = []
        next_states = []
        dones = []

        for s, a, r, ns, d in samples:
            states.append(s)
            actions.append(a)
            rewards.append(r)
            next_states.append(ns)
            dones.append(d)

        q_values = self.model.predict(np.vstack(states), batch_size=minibatch_size)
        target_values = self.target_model.predict(np.vstack(next_states), batch_size=minibatch_size)

        for i in range(len(samples)):
            if not dones[i]:
                y = rewards[i] + self.discounted_factor * np.amax(target_values[i])
            else:
                y = rewards[i]
            q_values[i][actions[i]] = y

        self.model.fit(x=np.stack(states), y=q_values, epochs=1, verbose=0, batch_size=minibatch_size)

"""
Model 
# """
# class DeepQNetwork(tf.keras.Model):
#     def __init__(self, state_size, action_size):
#         super(DeepQNetwork,self).__init__()
#         self.action_size = action_size
#         self.state_size = state_size
#
#         self.hidden1 = kl.Dense(128, activation='relu')
#         self.hidden2 = kl.Dense(128, activation='relu')
#         self.value = kl.Dense(action_size, name='value')
#
#     # this function will be called once it executes predict()
#     def call(self, inputs):
#         """
#         :param inputs: observation
#         :return:
#         """
#         x = tf.convert_to_tensor(inputs, dtype=tf.float32)
#         h = self.hidden1(x)
#         h = self.hidden2(h)
#         return self.value(h)


def build_network(state_size, action_size):

    input = tf.keras.Input(shape=(state_size,))
    h = kl.Dense(24, activation='relu',kernel_initializer='he_uniform')(input)
    h = kl.Dense(24, activation='relu',kernel_initializer='he_uniform')(h)
    output = kl.Dense(action_size, activation='linear',kernel_initializer='he_uniform')(h)
    model = Model(inputs=input, outputs=output)

    model.summary()
    model.compile(loss='mse', optimizer=Adam(lr=learning_rate))

    return model


# def build_network(state_size, action_size):
#     model = Sequential()
#     model.add(Dense(24, input_dim=state_size, activation='relu',
#                     kernel_initializer='he_uniform'))
#     model.add(Dense(24, activation='relu',
#                     kernel_initializer='he_uniform'))
#     model.add(Dense(action_size, activation='linear',
#                     kernel_initializer='he_uniform'))
#     model.summary()
#     model.compile(loss='mse', optimizer=Adam(lr=learning_rate))
#     return model


if __name__ == "__main__":

    EPISODES = 500
    TOTAL_STEP = 0

    env = gym.make('CartPole-v0')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    n_max_step = env._max_episode_steps
    s = env.reset()
    agent = Agent(state_size, action_size)

    # episode loop
    for e in range(EPISODES):  # loop until 500
        """episode start"""
        o = env.reset()
        R = 0
        d = False
        step = 0

        # inside episode
        while not d:
            TOTAL_STEP += 1
            step+=1

            action = agent.select_action(o)
            next_o, r, d, _ = env.step(action)

            if d and step < n_max_step-1:
                r = -100

            agent.append_sample(o, action, r, next_o, d)
            agent.train()

            R += r
            o = next_o

            if d:
                agent.update_target()

                if step < n_max_step-1:
                    R += 100
                print('{} episode, total steps : {}, return : {}'.format(e, TOTAL_STEP, R))
                break

