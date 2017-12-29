for _ in xrange(int(raw_input())):
    n = int(raw_input())
    colors = raw_input()
    arr = {'R': 0, 'G': 0, 'B': 0}
    for i in colors:
        arr[i] += 1
    print n - max(arr.values())
