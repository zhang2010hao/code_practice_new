

def lengthOfLIS(nums):
    # dp = [nums[0]]
    #
    # for i in range(1, len(nums)):
    #     if nums[i] >= dp[-1]:
    #         dp.append(nums[i])
    #     else:
    #         l, r = 0, len(dp) - 1
    #         loc = r
    #         while l <= r:
    #             m = (r + l) // 2
    #             if nums[i] > dp[m]:
    #                 l = m + 1
    #             else:
    #                 loc = m
    #                 r = m - 1
    #         dp[loc] = nums[i]
    #
    # return len(dp)

    n = len(nums)
    dp = [nums[0]]
    for i in range(1, n):
        if nums[i] > dp[-1]:
            dp.append(nums[i])
        else:
            l = 0
            r = len(dp) - 1
            loc = r
            while l <= r:
                m = (l + r) // 2
                if nums[i] > dp[m]:
                    l = m + 1
                else:
                    loc = m
                    r = m - 1

            dp[loc] = nums[i]
    return len(dp)

    # n = len(nums)
    # dp = [1] * n
    # for i in range(1, n):
    #     for j in range(0, i):
    #         if nums[j] < nums[i]:
    #             dp[i] = max(dp[j]+1, dp[i])
    #
    # return max(dp)

nums = [4,10,4,3,8,9]
rest = lengthOfLIS(nums)
print(rest)