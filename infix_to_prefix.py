def precedence(symbol):
    if symbol == '+' or symbol == '-':
        return 2
    if symbol == "*" or symbol == "/":
        return 4


if __name__ == "__main__":
    expression = raw_input()[::-1]
    stack = []
    prefix = []
    for i in expression:
        if i == "*" or i == "/" or i == "+" or i == "-":
            while stack and precedence(i) <= precedence(stack[len(stack)-1]):
                prefix.append(stack.pop())

            stack.append(i)
        else:
            prefix.append(i)

    while stack:
        prefix.append(stack.pop())

    print "".join(i for i in prefix[::-1])