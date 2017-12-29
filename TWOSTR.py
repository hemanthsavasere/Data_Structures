for _ in xrange(int(raw_input())):
    str1 = raw_input()
    str2 = raw_input()
    match = True
    for i in xrange(0, len(str1)):
        if str1[i] != '?' and str2[i] != '?' and str1[i] != str2[i]:
            match = False
            break

    if not match:
        print "No"

    else:
        print "Yes"
