for _ in xrange(int(raw_input())):
    n = raw_input()
    if n == n[::-1]:
        print "wins"
    else:
        print "losses"
