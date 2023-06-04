def findMedianSortedArrays(nums1, nums2):
    # def getKnum(k):
    #     offset1 = 0
    #     offset2 = 0
    #
    #     while True:
    #         if offset1 == n:
    #             return nums2[offset2 + k - 1]
    #         elif offset2 == m:
    #             return nums1[offset1 + k - 1]
    #         elif k == 1:
    #             return min(nums1[offset1], nums2[offset2])
    #
    #         new_offset1 = min(offset1 + k // 2 - 1, n - 1)
    #         new_offset2 = min(offset2 + k // 2 - 1, m - 1)
    #
    #         if nums1[new_offset1] <= nums2[new_offset2]:
    #             k = k - (new_offset1 - offset1 + 1)
    #             offset1 = new_offset1 + 1
    #         else:
    #             k = k - (new_offset2 - offset2 + 1)
    #             offset2 = new_offset2 + 1
    #
    # n, m = len(nums1), len(nums2)
    # if n == 0:
    #     if m % 2 == 0:
    #         return (nums2[m // 2] + nums2[m // 2 - 1])
    #     else:
    #         return nums2[m // 2]
    # elif m == 0:
    #     if n % 2 == 0:
    #         return (nums1[n // 2] + nums1[n // 2 - 1])
    #     else:
    #         return nums1[n // 2]
    # elif (m + n) % 2 == 0:
    #     return (getKnum((m + n) // 2) + getKnum((m + n) // 2 + 1)) / 2
    # else:
    #     return getKnum((m + n) // 2 + 1)

    # 寻找两个数组的第K大的元素
    def getKnum(k):
        offset1 = 0
        offset2 = 0

        while True:
            if k == 1:
                return max(nums1[offset1], nums2[offset2])
            elif k >= m:
                return nums1[offset1 + k - 1]
            elif k >= n:
                return nums2[offset2 + k - 1]

            new_offset1 = min(offset1 + k // 2 - 1, n - 1)
            new_offset2 = min(offset2 + k // 2 - 1, m - 1)
            v1 = nums1[new_offset1]
            v2 = nums2[new_offset2]
            if v1 > v2:
                k = k - (new_offset2 - offset2 + 1)
                offset2 = new_offset2 + 1
            else:
                k = k - (new_offset1 - offset1 + 1)
                offset1 = new_offset1 + 1

    n, m = len(nums1), len(nums2)


nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))
