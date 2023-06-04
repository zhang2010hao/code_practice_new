
def majorityElement(nums):
    count = 0
    x = None

    for n in nums:
        if count == 0:
            x = n

        if x == n:
            count += 1
        else:
            count -= 1

    return x