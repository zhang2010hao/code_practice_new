def threeSum(nums):
    sum2idx = {}
    n = len(nums)

    sort_nums = sorted(nums)
    for i in range(n):
        s = 0 - sort_nums[i]
        sum2idx[s] = i

    rst = []
    for i in range(n - 2):
        if i > 0 and sort_nums[i] == sort_nums[i - 1]:
            continue

        for j in range(i + 1, n - 1):
            if j > i + 1 and sort_nums[j] == sort_nums[j - 1]:
                continue

            s = sort_nums[i] + sort_nums[j]
            if s in sum2idx and sum2idx[s] > j:
                rst.append([sort_nums[i], sort_nums[j], sort_nums[sum2idx[s]]])

    return rst


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
