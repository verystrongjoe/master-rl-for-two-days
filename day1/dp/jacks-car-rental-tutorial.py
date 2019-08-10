"""
reference! : https://github.com/zy31415/jackscarrental

Jack's Cart Rental Problem

Jack manages two locations for a nationwide car rental company.
Each day, some number of customers arrive at each location to rent cars.
If Jack has a car available, he rents it out and is credited $10 by the national company.
If he is out of cars at that location, then the business is lost.

Car become available for renting the day after they are returned.
To help ensure that cars are available  where they are needed,
Jack can move them between the two locations overnight, at a cost of %2 per car moved.
We assume that the number of cars requested and returned at each location are Poisson random variables,
Suppose lambda is 3 and 4 for rental requests at the first and second locations and 3 and 2 for returns.
To simplify the problem slightly, we assume that there can be no more than 20 cars at each locations
(any additional cars are returned to the nationwide company, and thus disappear from the problem) and
a maximum of five cars can be moved from one location to the other in one night,

We take the discount rate to be gamma = 0.9 and formulate this as a continuing finite MDP,
where the time steps are days, the state is the number of cars at each location at the end of the day,
and the actions are the net numbers of cars moved between the two locations overnight.

Make this problem more likely to real world which is non stationary and arbitrary dynamics.
"""

import numpy as np
from day1.dp.possion import Possion

class PolicyIteration(object):

    n_max = 20
    rental_reward = 10
    moivng_cost = 2
    n_max_moving_cnt = 5
    bad_action_cost = 1000

    request_mean_1 = 3
    request_mean_2 = 4
    rental_mean_2 = 3
    rental_mean_2 = 2

    discount = 0.9
    threshold_error = 0.01
    policy = None
    value = None


    def __init__(self):
        self.policy = np.zeros([self.n_max+1] * 2, int)
        self.value = np.zeros([self.n_max+1] * 2)

        self._reward1 = self.expected_rental_reward(self.request_mean_1)
        self._reward2 = self.expected_rental_reward(self.rental_mean_2)

        assert self.bad_action_cost >= 0

    @classmethod
    def expected_rental_reward(cls, expected_reqeust):
        return np.asarray([cls._state_reward(s, expected_reqeust) for s in range(cls.n_max+1)])

    @classmethod
    def _state_reeward(cls, s, mu):
        rewards = cls.rental_reward * np.arange(s+1)
        p = Possion.pmf_series(mu, cutoff=s)
        return rewards.dot(p)

    def transition_probability(self, s, req, ret, action=0):
        """
        :param s: Current state
        :param req:  Mean value of request in a rental location
        :param ret:  Mean value of returns in a rental location
        :param action:  Action, Positive means move in. Negative means move out.
        :return: Transition probability
        """

        _ret_sz = self.n_max + self.n_max_moving_cnt

        p_req = Possion.pmf_series(req,s)
        p_ret = Possion.pmf_series(ret, _ret_sz)
        p = np.outer(p_req, p_ret)

        transp = np.asarray([p.trace(offset) for offset in range(-s, _ret_sz+1)])

        assert abs(action) <= self.n_max_moving_cnt, "action could not be larger than %s." % self.n_max_moving_cnt

        # No cars are being moved
        if action == 0:
            transp[20] += sum(transp[21:])
            return transp[:21]

        # Move cars from Location 1 to Location 2
        if action > 0:
            transp[self.n_max - action] += sum(transp[self.n_max -action +1:])
            transp[self.n_max -action + 1:] = 0
            return np.roll(transp, shift=action)[:self.n_max+1]


        # Move cars from Location 2 to Location 1
        action = -action
        transp[action] += sum(transp[:action])


















if __name__ == "__main__":
    """
    We take the discount rate to be gamma = 0.9 and formulate this as a continuing finite MDP,
    where the time steps are days, the state is the number of cars at each location at the end of the day,
    and the actions are the net numbers of cars moved between the two locations overnight.
    """
    gamma = 0.9

    first = Location(index=0)
    second = Location(index=1)

    day = 1
    income = 0

    # action policy function
    policy = np.zeros(shape=(N_MAX_CAR, N_MAX_CAR))

    # state-value function
    value = np.zeros(shape=(N_MAX_CAR, N_MAX_CAR))

    while True:
        request_for_first = get_request_for_first()
        request_for_second = get_reqeust_for_second()
        return_for_first = get_return_for_first()
        return_for_second = get_return_for_second()

        if first.do_rental(request_for_first) :
            income += request_for_first * RENTAL_INCOME
        else:  # in case of failure
            print('in first place, mission failed..')
            break

        if second.do_rental(request_for_second):
            income += request_for_second * RENTAL_INCOME
        else:  # in case of failure
            print('in second place, mission failed..')
            break

        first.do_return(return_for_first)
        second.do_return(return_for_second)

        # I am not sure whether or not Jack to move them between two locations overnight after cars are returned.

        # Policy Iteration start!!

        # Policy Evaluation
        for first in range(N_MAX_CAR):
            for second in range(N_MAX_CAR):
                v = value[first][second]
                value[first][second] =


        # Policy Improvement


        print('day : {}, income : {}, first : {}, second : {}'.format(day, income, first.n_available_car, second.n_available_car))
        day = day + 1
