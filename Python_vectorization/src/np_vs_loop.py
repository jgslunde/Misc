import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
def numpy_vs_for_loop(N=1e7):
    # Compares how numpy performs vs a for loop at a given number of iterations.
    N = int(N)
    print "Iterations = %d" % N
    a = np.linspace(0, 1, N)
    b = np.linspace(1, 2, N)
    c = np.zeros(N)

    time0 = time.time()
    for i in xrange(N):
        c[i] = a[i]*b[i]
    loop_time = time.time() - time0

    time0 = time.time()
    c = a*b
    numpy_time = time.time() - time0

    print "For loop time used = %.2f s" % (loop_time)
    print "Numpy time used = %.2f s" % (numpy_time)
    print "For loop FLOPS = %.2e" % (N/loop_time)
    print "Numpy FLOPS = %.2e" % (N/numpy_time)
    print "Numpy is %.2f times faster than a for loop" % (loop_time/numpy_time)

def numpy_vs_for_loop2(number_of_tests, N_list):
    # Compares how numpy performs against a for loop at an interval of iterations.
    loop_time = np.zeros(len(N_list))
    numpy_time = np.zeros(len(N_list))

    for j in xrange(number_of_tests):
        for x in range(len(N_list)):
            N = int(N_list[x])
            a = np.linspace(0, 1, N)
            b = np.linspace(1, 2, N)
            c = np.zeros(N)

            time0 = time.clock()
            for i in xrange(N):
                c[i] = a[i]*b[i]
            loop_time[x] += (time.clock() - time0)

            time0 = time.clock()
            c = a*b
            numpy_time[x] += (time.clock() - time0)

    numpy_time = numpy_time/number_of_tests
    loop_time = loop_time/number_of_tests
    numpy_improvement = loop_time/numpy_time
    print loop_time, numpy_time, numpy_improvement
    plt.plot(N_list, numpy_improvement)
    plt.ylabel("Numpy improvement factor")
    plt.xlabel("Number of computations")
    plt.show()

N_list = range(5, 100, 5) + range(100, 1000, 10) + range(1000, 10000, 200)
numpy_vs_for_loop2(50, np.array(N_list))
