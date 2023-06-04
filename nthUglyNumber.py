

def nthUglyNumber(n):
    if n == 1:
        return 1

    p1 = 0
    p2 = 0
    p3 = 0
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        num1, num2, num3 = 2 * dp[p1], 3 * dp[p2], 5 * dp[p3]
        dp[i] = min(num1, num2, num3)
        if dp[i] == num1:
            p1 += 1
        if dp[i] == num2:
            p2 += 1

        if dp[i] == num3:
            p3 += 1



    return dp[-1]

rst = nthUglyNumber(10)
print(rst)
