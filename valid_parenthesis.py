from collections import deque


def valid_parenthesis(s):
    d = {'{': '}', '[': ']', '(': ')', '<': '>'}
    stack = deque()
    for i in s:
        if i in d.keys():
            stack.append(i)
        elif i in d.values():
            try:
                if d[stack.pop()] == i:
                    continue
                else:
                    return False
            except IndexError:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


s = "((())){"
print(valid_parenthesis(s))
