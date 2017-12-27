for _ in xrange(int(raw_input())):
    n = int(raw_input())
    arr = dict()
    if n == 0:
        print "Draw"

    else:

        for i in xrange(n):
            k = raw_input()
            try:
                arr[k] += 1
            except:
                arr[k] = 1

        li = arr.keys()

        if len(li) == 1:
            print li[0]

        else:
            if arr[li[0]] == arr[li[1]]:
                print "Draw"

            elif arr[li[0]] > arr[li[1]]:
                print li[0]

            else:
                print li[1]
