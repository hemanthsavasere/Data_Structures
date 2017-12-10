import os
if __name__ == "__main__":
    formula = raw_input().strip()
    stack = []
    for i in formula:
        if i == "C" or i == "H" or i == "O":
            if i == "C":
                stack.append(12)
            if i == "H":
                stack.append(1)
            if i == "O":
                stack.append(16)

        if i.isdigit():
            num = stack.pop()
            res = int(num) * int(i)
            stack.append(res)

        if i == "(":
            stack.append(i)

        if i == ")":
            temp = 0
            while stack and stack[len(stack) - 1] != "(":
                temp += int(stack.pop())
            stack.pop()
            stack.append(temp)

    mass = 0
    while stack:
        mass += int(stack.pop())

    print mass

