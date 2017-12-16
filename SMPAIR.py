for _ in xrange(int(raw_input())):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    print arr[0]+arr[1]

