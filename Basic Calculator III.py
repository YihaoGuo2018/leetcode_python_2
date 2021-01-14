class Solution(object):
    def calculate(self, s):
        stack = []

        def update(op, num):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-1 * num)
            elif op == "*":
                tmp = stack.pop()
                stack.append(tmp * num)
            elif op == "/":

                tmp = stack.pop()

                stack.append((abs(tmp) / num) * (tmp / abs(tmp)))

        num = 0
        op = "+"
        for char in s:
            print(stack)
            if char.isdigit():

                num = num * 10 + int(char)
            elif char in ["+", "-", "*", "/"]:

                update(op, num)
                num = 0
                op = char
            elif char == ")":
                update(op, num)
                num = 0
                op = "+"
                tmp = 0
                while len(stack) and isinstance(stack[-1], int):
                    tmp += stack.pop()
                op = stack.pop()
                num = tmp
            elif char == "(":
                stack.append(op)
                num = 0
                op = "+"
        update(op, num)

        return sum(stack)
