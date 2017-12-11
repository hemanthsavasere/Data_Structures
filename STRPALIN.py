def palinstring(str1,str2):
    val = False
    s1 = []
    s2 = []
    for i in xrange(1, len(str1) + 1):
        s1.append(str1[0:i])
    print s1
    for i in xrange(1, len(str2) + 1):
        s2.append(str2[0:i])
    print s2
    for i in s1:
        for j in s2:
            if (i + j) == (i + j)[::-1]:
                val = True
                return val

    return val


for _ in xrange(int(raw_input())):
    ispalin = False
    str1 = raw_input()
    str2 = raw_input()
    print palinstring(str1,str2)
