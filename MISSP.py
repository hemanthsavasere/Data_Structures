from  collections import  defaultdict
for _ in xrange(int(raw_input())):
    n = int(raw_input())
    arr = defaultdict()
    for i in xrange(n):
        num = int(raw_input())
        try:
            arr[num] += 1
        except:
            arr[num] = 1

    for i in arr:
        if arr[i] % 2 != 0:
            print i