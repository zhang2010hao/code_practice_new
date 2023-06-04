def nextPermutation(nums):
    n = len(nums)
    if n == 1:
        return

    min_v = n - 1

    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            min_v = i
            break

    max_v = n - 1
    for i in range(n - 1, min_v, -1):
        if nums[i] > nums[min_v]:
            max_v = i
            break

    if min_v != max_v:
        nums[min_v], nums[max_v] = nums[max_v], nums[min_v]
        for i in range((n - 1 - min_v) // 2):
            nums[min_v + 1 + i], nums[n - 1 - i] = nums[n - 1 - i], nums[min_v + 1 + i]
    else:
        for i in range(n // 2):
            nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]

    return


nums = [3,2,1]
nextPermutation(nums)
