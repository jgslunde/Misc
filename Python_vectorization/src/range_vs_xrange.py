import numpy as np
import time


def range_vs_xrange(N=1e8):
    N = int(N)
    print "Iterations = %.1e" % N

    time0 = time.time()
    for i in range(N):
        pass
    range_time = time.time() - time0

    time0 = time.time()
    for i in xrange(N):
        pass
    xrange_time = time.time() - time0

    print "range iterations per second = %.2e" % (N/range_time)
    print "xrange iterations per second = %.2e" % (N/xrange_time)
    print "Time for range loop = %.2f" % range_time
    print "Time for xrange loop = %.2f" % xrange_time
    print "xrange is %.2f times faster than range" % (range_time/xrange_time)

range_vs_xrange()
