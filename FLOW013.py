for _ in xrange(int(raw_input())):
    a, b, c = map(int, raw_input().split())
    if a == 0 or b == 0 or c == 0 or a == 180 or b == 180 or c == 180:
        print "NO"
    elif a+b+c < 180 or a+b+c > 180:
        print "NO"
    else:
        print "YES"
