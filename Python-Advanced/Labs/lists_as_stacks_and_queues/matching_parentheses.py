expression = input()
parentheses_stack = []
for index in range(len(expression)):
    if expression[index] == '(':
        parentheses_stack.append(index)
    if expression[index] == ')':
        print(expression[parentheses_stack.pop():index + 1])
