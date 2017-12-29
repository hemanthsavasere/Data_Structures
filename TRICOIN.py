for _ in xrange(int(raw_input())):
    n = int(raw_input())
    ans = int((-1 + int((1 + 8 * n) ** 0.5)) / 2)
    print ans
