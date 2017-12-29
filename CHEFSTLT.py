for _ in xrange(int(raw_input())):
    str1 = raw_input()
    str2 = raw_input()

    min_mismatch, max_mismatch = 0, 0

    for i in xrange(len(str1)):
        if str1[i] != '?' and str2[i] != '?' and str1[i] != str2[i]:
            min_mismatch += 1

    for i in xrange(len(str1)):
        if str1[i] == '?' or str2[i] == '?' or str1[i] != str2[i]:
            max_mismatch += 1

    print min_mismatch, max_mismatch