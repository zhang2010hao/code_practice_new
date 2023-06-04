def maxSlidingWindow(nums, k):
    # rst = []
    # n = len(nums)
    # if k >= n:
    #     rst.append(max(nums))
    #     return rst
    #
    # dq = []
    # for i in range(k):
    #     while len(dq) > 0 and nums[i] >= nums[dq[-1]]:
    #         dq.pop(-1)
    #     dq.append(i)
    #
    # rst.append(nums[dq[0]])
    #
    # for i in range(k, n):
    #     while len(dq) > 0 and nums[i] >= nums[dq[-1]]:
    #         dq.pop(-1)
    #     dq.append(i)
    #
    #     while len(dq) > 0 and dq[0] <= i - k:
    #         dq.pop(0)
    #
    #     rst.append(nums[dq[0]])
    #
    # return rst



    # rst = []
    # n = len(nums)
    # if k >= n:
    #     rst.append(max(nums))
    #     return rst
    #
    # que = []
    # for i in range(k):
    #     while len(que) > 0 and nums[i] >= nums[que[-1]]:
    #         que.pop(-1)
    #     que.append(i)
    #
    # rst.append(nums[que[0]])
    # for i in range(k, n):
    #     while len(que) > 0 and nums[i] >= nums[que[-1]]:
    #         que.pop(-1)
    #     que.append(i)
    #
    #     while len(que) > 0 and que[0] <= i - k:
    #         que.pop(0)
    #
    #     rst.append(nums[que[0]])
    #
    # return rst

    # 单调队列
    que = []
    rest = []
    n = len(nums)
    for i in range(k):
        while len(que) > 0 and nums[i] >= nums[que[-1]]:
            que.pop(-1)

        que.append(i)

    rest.append(nums[que[0]])

    for i in range(k, n):
        while len(que) > 0 and nums[i] >= nums[que[-1]]:
            que.pop(-1)

        que.append(i)

        while len(que) > 0 and que[0] < i - k + 1:
            que.pop(0)

        rest.append(nums[que[0]])

    return rest






nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

rst = maxSlidingWindow(nums, k)
print(rst)
