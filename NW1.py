for _ in xrange(int(raw_input())):
    n, day = raw_input().split()
    arr = {"mon": 4, "tues": 4, "wed": 4, "thurs": 4, "fri": 4, "sat": 4, "sun": 4}
    brr = ["mon", "tues", "wed", "thurs", "fri", "sat", 'sun']
    n = int(n)-28
    for i in xrange(0,n):
        arr[day] += 1
        day = brr[(brr.index(day)+1)%7]

    print " ".join(str(arr[day]) for day in brr)