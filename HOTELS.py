if __name__ == "__main__":
    n, m = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    maxi = 0
    k, total = 0, 0
    for i in arr:
        total += i
        print "total is", total, i

        if total > maxi and total <= m:
            maxi = total

        while total > m:
            total -= arr[k]
            #print "reduction total is", total
            if total > maxi and total <= m:
                maxi = total
            k += 1
    print maxi
