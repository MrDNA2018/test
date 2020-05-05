#%%
import re


def toBack(s):  # 转后缀表达式
    stack = []
    res = []
    d = {}
    d['+'] = 1
    d['-'] = 1
    d['*'] = 2
    d['/'] = 2
    d['('] = 0
    pattern = re.compile(r"([()\+\*/-])")
    s = re.split(pattern, s)
    for e in s:
        if e in '+-*/()':
            if e == "":
                continue
            if e == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    res.append(stack.pop())
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
            elif e == '(':
                stack.append(e)
            else:
                while len(stack) > 0 and d[stack[-1]] >= d[e]:
                    res.append(stack.pop())
                stack.append(e)
        else:
            res.append(e)
    res += stack[::-1]
    return res


def calculator(l):
    stack = []
    for e in l:
        if e in "+-*/":
            if stack:
                b = int(stack.pop())
                if stack:
                    a = int(stack.pop())
                    if e == '+':
                        stack.append(a + b)
                    elif e == '-':
                        stack.append(a - b)
                    elif e == '*':
                        stack.append(a * b)
                    elif e == '/':
                        stack.append(a / b)
                else:
                    if e == '-':
                        stack.append(0-b)

        else:
            stack.append(e)
    return stack[0]


s = input()
l = toBack(s)
print(calculator(l))
range()