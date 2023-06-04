

def twoSum(nums, target):
    cha2idx = {}
    for i, num in enumerate(nums):
        if num in cha2idx:
            return [cha2idx[num], i]
        else:
            cha2idx[target - num] = i

    return []