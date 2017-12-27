word = raw_input()
for _ in xrange(int(raw_input())):
    alpha = raw_input()
    not_known = False
    for i in alpha:
        if i not in word:
            not_known = True
            break
    if not_known :
        print("No")
    else:
        print("Yes")