

def constrainedSubsetSum(nums, k):
    n = len(nums)
    # dp的含义是第i个位置选择第二个元素后的数组值
    dp = [nums[0]] + [0] * (n-1)

    q = [0]

    rst = nums[0]
    for i in range(1, n):

        while len(q) > 0 and i - q[0] > k:
            q.pop(0)

        dp[i] = max(0, dp[q[0]]) + nums[i]
        rst = max(dp[i], rst)

        while len(q) > 0 and dp[i] >= dp[q[-1]]:
            q.pop(-1)

        q.append(i)

    return rst

numbers = [-7609,249,-1699,2385,9125,-9037,1107,-8228,856,-9526]
k = 9
rest = constrainedSubsetSum(numbers, k)
print(rest)