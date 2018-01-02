for _ in xrange(int(raw_input())):
    n, m = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    arr.sort()
    print "%.6f" % (sum(arr[m:n-m])/((n*1.0)-(2.0*m)))