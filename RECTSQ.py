from math import sqrt
def max_squares(m, n):
    if n > m:
        n ,m = m, n
    c, d = m, n

    if n == 0:
        return m
    else:
        while n > 0:
            rem = m % n
            m = n
            n = rem
        return (c/m)*(d/m)

if __name__=="__main__":
    for i in xrange(int(raw_input())):
        a, b = map(int, raw_input().split())
        print max_squares(a,b)