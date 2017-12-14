n = 1
while n != 0:
    n = int(raw_input())
    if n == 0:
        break
    arr = map(int, raw_input().split())
    brr = [None] * (n + 1)
    k = 1
    i = 0
    while k <= n:
        brr[arr[i]] = k
        k += 1
        i += 1

    if brr[1:] == arr :
        print "ambiguous"

    else:
        print "not ambiguous"
