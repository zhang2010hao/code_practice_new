def trap(height):
    n = len(height)
    leftmax = [0] * n
    leftmax[0] = height[0]

    rightmax = [0] * n
    rightmax[n - 1] = height[-1]

    for i in range(1, n):
        leftmax[i] = max(height[i], leftmax[i - 1])
        rightmax[n - 1 - i] = max(height[n - 1 - i], rightmax[n - i])

    rest = 0
    for i in range(1, n - 1):
        rest = rest + min(leftmax[i], rightmax[i]) - height[i]

    return rest