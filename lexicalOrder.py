def lexicalOrder(n):
    rest = [0] * n

    num = 1
    for i in range(n):
        rest[i] = num
        if num * 10 < n:
            num = num * 10
        else:
            if num % 10 == 9 or num == n:
                num = num // 10

            num += 1

    return rest

print(lexicalOrder(200))