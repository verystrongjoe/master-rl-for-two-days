"""
A gambler has the opportunity to make bets on the outcomes of a sequence of coin flips.
If the coin comes up heads, he wins as many dollars as he has staked on that flip;
if it is tails, he loses his stake.

The game ends when the gambler wins by reaching his goal of $100, or loses by running out of money.
On each flip, the gambler must decide what portion of his capital to stake, in integer numbers of dollars.
This problem can be formulated as an undiscounted, episodic, finite MDP.
The state is the gambler’s capital,  s belongs {1, 2, . . . , 99} and the actions
are stakes, a belongs {0, 1, . . . , min(s, 100− s)}.
The reward is zero on all transitions except those on which the gambler reaches his goal, when it is +1.

The state-value function then gives the probability of winning from each state. A policy is a mapping from
levels of capital to stakes. The optimal policy maximizes the probability of reaching the goal.
Let ph denote the probability of the coin coming up heads. If ph is known, then the entire problem is known
and it can be solved, for instance, by value iteration.

Figure 4.3 shows the change in the value function over successive sweeps of value iteration,
and the final policy found, for the case of ph = 0.4. This policy is optimal, but not unique.
Infact, there is a whole family of optimal policies, all corresponding to ties for the argmax action
selection with respect to the optimal value function. Can you guess what the entire family looks like?

https://github.com/dennybritz/reinforcement-learning/blob/master/DP/Gamblers%20Problem%20Solution.ipynb

"""

import numpy as np
import sys
import matplotlib.pyplot as plt

# state  0~ 99
# actions = 0 ~ min(s, 100-s)
# reward 0 except when gambler reaches his goal +1

# state-value function : the probability of winning from each state
# policy is a mapping levels of capital to stake
# optimal policy --> maximizes the probability of reaching the goal
# ph --> probability of the coin coming up heads!!


gamma = 1.0
ph = 0.4
#small threshold value for comparing between estimated and real value function
theta = 0.00001


n_observation_space = 100

reward = [0 for _ in range(n_observation_space+1)]
reward[n_observation_space] = 1


value = [0 for _ in range(n_observation_space+1)]
policy = [0 for _ in range(n_observation_space+1)]



def rollout():
    delta = 1

    while delta > theta:
        delta = 0
        "Looping over all the states i.e the money in hand for a current episode"
        for i in range(1, n_observation_space):
            oldvalue = value[i]
            bellmanoptimalequation(i)
            diff = abs(oldvalue - value[i])
            delta = max(delta, diff)
        print(value)
        print(policy)
    plt.plot(policy)
    plt.show()
    plt.plot(value)
    plt.show()


def bellmanoptimalequation(num):
    optimalvalue = 0

    "The range of number of bets"
    for stake in range(1, min(num, 100-num)+1):
        "Amount after winning and loosing"
        win = num + stake
        loss = num - stake
        "calculate the average of possible states for an action"
        "In this case it would be Head or Tails"
        sum = ph * (reward[win] + gamma * value[win]) + (1 - ph) * (reward[loss] + gamma * value[loss])

        "Choose the action that gives the max reward and update the policy and value for that"
        if sum > optimalvalue:
            optimalvalue = sum
            value[num] = sum
            policy[num] = stake

if __name__=="__main__":
    rollout()