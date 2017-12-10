def precedence(symbol):
    if symbol == "+" or symbol == "-":
        return 2
    elif symbol == "*" or symbol == "/":
        return 4


if __name__ == "__main__":
    infix = raw_input()
    stack = []
    postfix = []
    for i in infix:
        if i == "(":
            stack.append(i)

        elif i == ")":
            while stack and stack[len(stack)-1] != "(":
                postfix.append(stack.pop())
                print postfix, stack
            stack.pop()

        elif i == "+" or i == "-" or i == "*" or i == "/":

            while stack and precedence(i) <= precedence(stack[len(stack) - 1]) :
                postfix.append(stack.pop())
                print stack

            stack.append(i)
            print stack, postfix

        else:
            postfix.append(i)

    while stack:
        postfix.append(stack.pop())

    print stack, "".join(str(i) for i in postfix)
