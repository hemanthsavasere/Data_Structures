for _ in xrange(int(raw_input())):
    m, n = map(int, raw_input().split())
    if n > m:
        m, n = n, m
    num1 , num2 = m, n

    while n != 0:
        rem = m % n
        m = n
        n = rem

    print m,(num1 * num2)/m
