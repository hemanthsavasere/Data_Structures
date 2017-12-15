from math import sqrt
arr = [i for i in xrange(0, 100001)]

for i in xrange(2, int(sqrt(100001)) + 1):
    if arr[i] is not None:
        arr[i] = i
        j = i * 2
        while j < 100001:
            arr[j] = None
            j += i

brr = [i for i in arr[2:] if i is not None ]

for _ in xrange(int(raw_input())):
    n = int(raw_input())
    if n in brr:
        print "yes"
    else:
        print "no"
