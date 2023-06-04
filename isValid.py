
def isValid(s):
    q1 = []

    for c in s:
        if c == '(':
            q1.append(c)
        elif c == ')':
            if len(q1) < 1:
                return False
            else:
                tmp_c = q1.pop(-1)
                if tmp_c != '(':
                    return False
        elif c == '[':
            q1.append(c)
        elif c == ']':
            if len(q1) < 1:
                return False
            else:
                tmp_c = q1.pop(-1)
                if tmp_c != '[':
                    return False
        elif c == '{':
            q1.append(c)
        elif c == '}':
            if len(q1) < 1:
                return False
            else:
                tmp_c = q1.pop(-1)
                if tmp_c != '{':
                    return False
    if len(q1) > 0:
        return False
    else:
        return True

s = '(]'
print(isValid(s))
