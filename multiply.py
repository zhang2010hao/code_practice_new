def multiply(num1, num2):
    def numadd(n1, n2):
        m1 = len(n1)
        m2 = len(n2)
        m = max(m1, m2)
        if len(n1) < len(n2):
            arr = ['0'] * (m2 - m1)
            n1 = ''.join(arr) + n1
        elif len(n1) > len(n2):
            arr = ['0'] * (m1 - m2)
            n2 = ''.join(arr) + n2

        rst = ''
        jinwei = 0
        for i in range(m - 1, -1, -1):
            tmp = int(n1[i]) + int(n2[i]) + jinwei
            if tmp >= 10:
                jinwei = 1
                tmp = tmp - 10
            else:
                jinwei = 0

            rst = str(tmp) + rst

        if jinwei > 0:
            rst = str(jinwei) + rst

        return rst

    def multical(s1, s2):
        s1 = int(s1)
        rst = ''
        m = len(s2)
        jinwei = 0
        flag = False
        for i in range(m - 1, -1, -1):
            tmp = int(s2[i]) * s1 + jinwei
            jinwei = tmp // 10
            tmp = tmp % 10
            rst = str(tmp) + rst
            if jinwei > 0 or tmp > 0:
                flag = True

        if jinwei > 0:
            rst = str(jinwei) + rst

        return rst, flag


    l1 = len(num1)
    l2 = len(num2)
    if l1 < l2:
        num1, num2 = num2, num1
        l1, l2 = l2, l1

    rest = ''
    for i in range(l2):
        arr = ['0'] * i
        s, flag = multical(num2[l2-1-i], num1)
        if flag:
            s = s + ''.join(arr)
            rest = numadd(rest, s)

    if rest == '':
        rest = '0'

    return rest

num1 = "9999"
num2 = "0"
print(multiply(num1, num2))

