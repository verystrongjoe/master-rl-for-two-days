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

# Suppose lambda is 3 and 4 for rental requests at the first and second locations and 3 and 2 for returns.
def get_request_for_first():
    return np.random.poisson(3, 10)[0]

RENTAL_INCOME = 10
MOVE_COST = 2
N_MAX_CAR = 20
N_MAX_AVAILABLE_MOVE_CAR = 5

N_STARTING_CNT_CAR_FIRST = 20
N_STARTING_CNT_CAR_SECOND = 20

class Location:
    def __init__(self, index):
        self.index = index
        if index == 0:
            self.n_available_car = N_STARTING_CNT_CAR_FIRST
        elif index == 1:
            self.n_available_car = N_STARTING_CNT_CAR_SECOND
        else:
            raise Exception("No case")

    def do_return(self, n):
        # any additional cars are returned to the nationwide company, and thus disappear from the problem
        self.n_available_car = max(N_MAX_CAR, self.n_available_car + n)

    def do_rental(self, n):
        if self.n_available_car >= n:
            self.n_available_car = self.n_available_car - n
            return True
        else:
            return False


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

        print('day : {}, income : {}, first : {}, second : {}'.format(day, income, first.n_available_car, second.n_available_car))
        day = day + 1