for _ in xrange(int(raw_input())):
    n, m, k = map(int,raw_input().split())
    arr1 = set(map(int,raw_input().split()))
    arr2 = set(map(int,raw_input().split()))
    print len(arr1.intersection(arr2)), n-len(arr1.union(arr2))