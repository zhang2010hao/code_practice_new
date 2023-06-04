def calculate(s):
    # n = len(s)
    # s = s.replace(' ', '').replace('(-', '(0-')
    #
    # if n < 3:
    #     return int(s)
    #
    # kh = []
    # que = []
    # for i, c in enumerate(s):
    #     if c == '(':
    #         que.append(i)
    #     elif c == ')':
    #         kh.append((que.pop(-1), i))
    #
    # for t in kh:
    #     if t[0] == 0:
    #         s = ' ' + s[1:t[1]] + ' ' + s[t[1] + 1:]
    #     else:
    #         if s[t[0] - 1] == '-':
    #             tmp = ' '
    #             for i in range(t[0] + 1, t[1]):
    #                 if s[i] == '+':
    #                     tmp = tmp + '-'
    #                 elif s[i] == '-':
    #                     tmp = tmp + '+'
    #                 else:
    #                     tmp = tmp + s[i]
    #             tmp = tmp + ' '
    #             s = s[:t[0]] + tmp + s[t[1] + 1:]
    #         else:
    #             s = s[:t[0]] + ' ' + s[t[0] + 1:t[1]] + ' ' + s[t[1] + 1:]
    #
    # s = s.replace(' ', '')
    # n = len(s)
    # arr = []
    # l, r = 0, 0
    # if s[0] == '-':
    #     r += 1
    #     while s[r] != '-' and s[r] != '+':
    #         r += 1
    #     arr.append(s[l:r])
    #     l = r
    #
    # while l <= r and l < n and r < n:
    #     if s[r] == '-' or s[r] == '+':
    #         if r > l:
    #             arr.append(s[l:r])
    #
    #         arr.append(s[r])
    #
    #         r += 1
    #         l = r
    #     else:
    #         r += 1
    #
    # if l != r:
    #     arr.append(s[l:r])
    #
    # rst = 0
    # i = 0
    # while i < len(arr):
    #     if arr[i] == '-':
    #         rst = rst - int(arr[i + 1])
    #         i = i + 2
    #     elif arr[i] == '+':
    #         rst = rst + int(arr[i + 1])
    #         i = i + 2
    #     elif len(arr[i]) > 0:
    #         rst = rst + int(arr[i])
    #         i = i + 1
    #     else:
    #         i += 1
    #
    # return rst

    s = s.replace(' ', '').replace('(-', '(0-')
    if s[0] == '-':
        s = '0' + s

    n = len(s)
    if n < 3:
        return int(s)

    kh = []
    que = []
    for i, c in enumerate(s):
        if c == '(':
            que.append(i)
        elif c == ')':
            kh.append((que.pop(-1), i))

    for t in kh:
        if t[0] == 0:
            s = ' ' + s[1:t[1]] + ' ' + s[t[1] + 1:]
        else:
            if s[t[0] - 1] == '-':
                tmp = ' '
                for i in range(t[0] + 1, t[1]):
                    if s[i] == '+':
                        tmp = tmp + '-'
                    elif s[i] == '-':
                        tmp = tmp + '+'
                    else:
                        tmp = tmp + s[i]
                tmp = tmp + ' '
                s = s[:t[0]] + tmp + s[t[1] + 1:]
            else:
                s = s[:t[0]] + ' ' + s[t[0] + 1:t[1]] + ' ' + s[t[1] + 1:]

    s = s.replace(' ', '')
    n = len(s)
    arr = []
    l, r = 0, 0

    while l <= r and l < n and r < n:
        if s[r] == '-' or s[r] == '+':
            if r > l:
                arr.append(s[l:r])

            arr.append(s[r])

            r += 1
            l = r
        else:
            r += 1

    if l != r:
        arr.append(s[l:r])

    rst = 0
    i = 0
    while i < len(arr):
        if arr[i] == '-':
            rst = rst - int(arr[i + 1])
            i = i + 2
        elif arr[i] == '+':
            rst = rst + int(arr[i + 1])
            i = i + 2
        elif len(arr[i]) > 0:
            rst = rst + int(arr[i])
            i = i + 1
        else:
            i += 1

    return rst




N = 1 + 1
print(N)
s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))
