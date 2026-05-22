import numpy as np

def levy_step(alpha):

    u = np.random.standard_cauchy(size=3)

    u *= np.random.rand()**(-1/alpha)

    return u
