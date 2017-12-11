

for _ in xrange(int(raw_input())):
    str1 = set(raw_input())
    str2 = set(raw_input())

    if str1.intersection(str2):
        print "Yes"
    else:
        print "No"
