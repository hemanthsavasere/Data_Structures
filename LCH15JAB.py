for _ in xrange(int(raw_input())):
    arr = [0] * 26
    string = raw_input()
    for i in string:
        arr[ord(i)-97] += 1

    arr.sort()
    k = len(arr)

    if sum(arr[:k-1]) == sum(arr[k-1:]):
        print "YES"
    else:
        print "NO"
