for _ in xrange(int(raw_input())):
    n = int(raw_input())
    arr1 = map(int,raw_input().split())
    arr2 = map(int,raw_input().split())
    maxi, rating = 0, 0

    for i in xrange(n):
        if arr1[i]*arr2[i] >= arr1[maxi]*arr2[maxi] and arr2[i] > arr2[rating]:
            maxi = i
            rating = i

    print maxi+1