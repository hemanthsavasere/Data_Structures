for _ in xrange(int(raw_input())):
    dist = int(raw_input())
    x1, y1 = map(int, raw_input().split())
    x2, y2 = map(int, raw_input().split())
    x3, y3 = map(int, raw_input().split())

    d1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    d2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    d3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

    if (d1 <= dist and d2 <= dist) or (d2 <= dist and d3 <= dist) or (d3 <= dist and d1 <= dist):
        print "yes"
    else:
        print "no"
