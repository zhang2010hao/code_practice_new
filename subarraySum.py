

def subarraySum(nums, k):
    n = len(nums)
    num2cnt = {}
    # 出现和为0时起到初始化的作用
    num2cnt[0] = 1

    rest = 0
    s = 0
    for i in range(n):
        s += nums[i]

        if s - k in num2cnt:
            rest += num2cnt[s-k]

        num2cnt[s] = num2cnt.get(s, 0) + 1

    return rest