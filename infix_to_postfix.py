def precedence(symbol):
    if symbol == "+" or symbol == "-":
        return 2
    if symbol == "*" or symbol == "/":
        return 4
    if symbol == "^":
        return 8


if __name__ == "__main__":
    for _ in xrange(int(raw_input())):
            infix = raw_input()
            stack = []
            postfix = []
            for i in infix:
                if i == "(":
                    stack.append(i)

                elif i == ")":
                    while stack and stack[len(stack)-1] != "(":
                        postfix.append(stack.pop())

                    stack.pop()

                elif i == "+" or i == "-" or i == "*" or i == "/" or i == "^":

                    while stack and precedence(i) <= precedence(stack[len(stack) - 1]) :
                        postfix.append(stack.pop())


                    stack.append(i)

                else:
                    postfix.append(i)

            while stack:
                postfix.append(stack.pop())

            print "".join(str(i) for i in postfix)
