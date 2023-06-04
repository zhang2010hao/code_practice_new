def myAtoi(s):
    sign = 1
    n = len(s)
    if n == 0:
        return 0

    start = 0
    if s[0] == ' ':
        for j in range(1, n):
            if s[j] != ' ':
                start = j
                break

    sign_cnt = 0
    digit_flag = True
    rest = 0
    for i in range(start, n):
        if sign_cnt > 1:
            break

        if digit_flag and s[i] == '+':
            sign_cnt += 1
            continue
        elif digit_flag and s[i] == '-':
            sign_cnt += 1
            sign = -1
        elif s[i].isdigit():
            digit_flag = False
            rest = rest * 10 + int(s[i])
        elif not s[i].isdigit():
            break

    if rest == '':
        return 0
    else:
        rest = sign * int(rest)
        if rest > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif rest < -2 ** 31:
            return -2 ** 31
        else:
            return rest


print(myAtoi('00000-42a1234'))
