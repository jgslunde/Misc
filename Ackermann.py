import sys
sys.setrecursionlimit(10000)
recurses = 0
def ackermann(m, n):
    global recurses
    recurses += 1
    print "Calling ackerman for the %d time as Ackermann(%d,%d)" % (recurses, m, n)
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

print ackermann(4,4)
