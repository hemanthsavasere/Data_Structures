for _ in xrange(int(raw_input())):

    bracket = raw_input()
    balance = 0
    max_balance = 0

    for i in bracket:

        if i == "(":
            balance += 1

        if i == ")":
            balance -= 1

        if balance > max_balance:
            max_balance = balance

    print ("("*max_balance)+(")"*max_balance)
