for _ in xrange(int(raw_input())):
    n = int(raw_input())
    arr = [100, 50, 10, 5, 2, 1]
    cnt = 0
    i = 0
    while n != 0 and i < 7:
        if arr[i] <= n:
            n -= arr[i]
            cnt += 1
        else:
            i += 1
    print cnt