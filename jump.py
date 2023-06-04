def jump(nums):
    n = len(nums)
    maxPos, end, step = 0, 0, 0
    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                # 这一步的含义是让前面最长的一步走完后，再去更新最新能够达到的最远的位置
                end = maxPos
                step += 1
    return step


nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
print(jump(nums))


