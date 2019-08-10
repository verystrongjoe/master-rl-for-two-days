from scipy.stats import poisson
import numpy as np


# https://github.com/zy31415/jackscarrental
class Possion(object):

    cache_pmf = {}
    cache_sf = {}
    cache = {}
    MAX_CUTOFF = 25
    cache_enable = True

    @classmethod
    def pmf_series(cls, mu, cutoff):
        assert isinstance(mu, int), "mu should be an integer."
        assert isinstance(cutoff, int), "cutoff should be an integer"

        if (mu, cutoff) not in cls.cache:
            cls._calculate_pmf_series(mu, cutoff)

        return cls.cache[(mu, cutoff)]

    @classmethod
    def _calculate_pmf_series(cls, mu, cutoff):

        if mu not in cls.cache_pmf:
            cls.cache_pmf[mu] = poisson.pmf(np.arange(cls.MAX_CUTOFF +1), cutoff)
            cls.cache_sf[mu] = poisson.sf(np.arange(cls.MAX_CUTOFF+1), cutoff)

        out = np.copy(cls.cache_pmf[mu][:cls.MAX_CUTOFF+1])
        out[-1] += cls.cache_sf[mu][cls.MAX_CUTOFF]

        cls.cache[(mu, cutoff)] = out