from numpy import linspace, zeros, exp, sqrt, array, arange, abs, ones, float64, float128
from math import factorial, pi
import matplotlib.pyplot as plt

limit = 170
Ns = arange(0, limit, dtype=float128)

N_fac_actual = ones(limit)
for N in xrange(limit):
	N_fac_actual[N] = factorial(N)


N_fac_approx = Ns**Ns*exp(-Ns)*sqrt(2*pi*Ns)

error = abs(N_fac_approx - N_fac_actual)/N_fac_actual


plt.loglog(N_fac_actual, "r-")
plt.loglog(N_fac_approx, "b-")
plt.show()
plt.loglog(error)
plt.title("Relative error of Stirling's Approximation")
plt.xlabel("Factorial number N")
plt.ylabel("Relative error")
plt.show()
