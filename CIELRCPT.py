def menu(n):
    cnt = 0
    i = 11
    while n != 0 and i >= 0:
        if 2**i <= n:
            n = n - (2 ** i)
            cnt += 1
        else:
            i -= 1
    return cnt


if __name__ == "__main__":
    for _ in xrange(int(raw_input())):
        num = int(raw_input())
        k = menu(num)
        print (k)

