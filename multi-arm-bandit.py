"""
# reference
http://hub.zum.com/kimws/2586

"""

# use this problem to introudct a number of basic learning method which we
# extend in later chapters to apply to thee full reinforcement learning problem.

# when the bandit problem become associative, that is, when action are taken in more than one situations.

import numpy as np
import scipy as sp
import random


class SAB:
    def __init__(self, itemid, posProb):
        self.K = len(itemid))