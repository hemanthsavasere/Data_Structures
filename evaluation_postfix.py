def operation(operand, operator1, operator2):
    if operand == "+":
        return operator1 + operator2

    if operand == "-":
        return operator2 - operator1

    if operand == "*":
        return operator1 * operator2

    if operand == "/":
        if operator2 == 0:
            return float('inf')
        else:
            return operator1 / operator2


if __name__ == "__main__":
    expression = raw_input()
    operators = "+-*/"
    stack = []
    for i in expression:

        if i not in operators:
            stack.append(i)

        else:
            a = stack.pop()
            b = stack.pop()
            res = operation(i, int(a), int(b))
            stack.append(res)

        print stack
