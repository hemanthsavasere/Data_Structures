for _ in xrange(int(raw_input())):
    m, n = map(int, raw_input().split())

    if m <= 3:

        before_prime = [i for i in xrange(0, n+1)]
        before_prime[0] = 0
        before_prime[1] = 0

        for i in xrange(2, int((n + 1) ** 0.5 + 1)):
            if before_prime[i]:
                k = i * 2
                before_prime[k] = False
                while k <= n:
                    before_prime[k] = False
                    k += i

        for i in xrange(m, len(before_prime)):
            if before_prime[i]:
                print before_prime[i]
        print

    else:

        before_prime = [i for i in xrange(0, m+1)]
        before_prime[0] = 0
        before_prime[1] = 0
        brr = []

        for i in xrange(2, int(m ** 0.5 + 1)):
            if before_prime[i]:
                k = i * 2
                while k <= m:
                    before_prime[k] = 0
                    k += i

        for i in xrange(len(before_prime)):
            if before_prime[i]:
                brr.append(i)

        arr = [i for i in xrange(m, n + 1)]

        for i in brr:
            k = (m / i) * i
            while k < m:
                k += i
            while k <= n:
                if arr[k - m]:
                    arr[k - m] = 0
                k += i
        k = brr[len(brr)-1]
        if k >= m:
            arr.insert(0, k)

        for i in arr:
            if i:
                print i
        print