def merge(nums1, m, nums2, n):
    if m > 0:
        for i in range(m - 1, -1, -1):
            nums1[i], nums1[n + i] = nums1[n + i], nums1[i]

    idx1 = n
    idx2 = 0
    idx = 0
    while idx1 < m + n and idx2 < n:
        if nums1[idx1] <= nums2[idx2]:
            nums1[idx] = nums1[idx1]
            idx += 1
            idx1 += 1
        else:
            nums1[idx] = nums2[idx2]
            idx += 1
            idx2 += 1

    if idx2 < n:
        for i in range(idx2, n):
            nums1[idx] = nums2[i]
            idx += 1
    else:
        for i in range(idx1, m + n):
            nums1[idx] = nums1[i]
            idx += 1

    return


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print()
