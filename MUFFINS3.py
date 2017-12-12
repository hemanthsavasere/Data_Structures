for _ in xrange(0,int(raw_input())):
    n = int(raw_input())
    if n == 1:
        print 1
    elif n % (n/2 + 1) >= n % (n/2):
        print n/2 + 1
    else:
        print n/2



