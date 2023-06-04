def findKthLargest(nums, k):
    # 快速排序方案
    # def quicksort(arr, left, right):
    #     if left < right:
    #         m = partition(arr, left, right)
    #         if m == n - k:
    #             return arr
    #         elif n - k > m:
    #             quicksort(arr, m + 1, right)
    #         else:
    #             quicksort(arr, left, m - 1)
    #
    #
    # def partition(arr, left, right):
    #     if left < right:
    #         i = left - 1
    #         for j in range(left, right):
    #             if arr[j] < arr[right]:
    #                 i += 1
    #                 arr[i], arr[j] = arr[j], arr[i]
    #
    #         arr[i+1], arr[right] = arr[right], arr[i+1]
    #
    #     return i + 1
    #
    # n = len(nums)
    # quicksort(nums, 0, n-1)

    # 堆排序方案
    # def heap_max(arr, root, arr_len):
    #     larger_idx = root
    #     if 2 * root + 1 < arr_len and arr[2 * root + 1] > arr[larger_idx]:
    #         larger_idx = 2 * root + 1
    #
    #     if 2 * root + 2 < arr_len and arr[2 * root + 2] > arr[larger_idx]:
    #         larger_idx = 2 * root + 2
    #
    #     if larger_idx != root:
    #         arr[root], arr[larger_idx] = arr[larger_idx], arr[root]
    #         heap_max(arr, larger_idx, arr_len)
    #
    # def heapsort(arr):
    #     for i in range(n - 1, -1, -1):
    #         heap_max(arr, i, n)
    #
    #     for i in range(n - 1, n - 1 - k, -1):
    #         arr[i], arr[0] = arr[0], arr[i]
    #         heap_max(arr, 0, i)
    #
    # n = len(nums)
    # heapsort(nums)
    #
    # return nums[-k]



nums = [3, 2, 1, 5, 6, 4]
k = 4
print(findKthLargest(nums, k))
