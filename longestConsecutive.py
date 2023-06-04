def longestConsecutive(nums):
    num_set = set(nums)
    rest = 0

    for num in nums:
        if num - 1 not in num_set:
            cur = num
            l = 1

            while cur + 1 in num_set:
                cur += 1
                l += 1

            rest = max(rest, l)

    return rest