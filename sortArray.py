
def sortArray(nums):
    def partition(arr, left, right):
        pivot = arr[right]
        idx = left - 1
        for i in range(left, right):
            if arr[i] < pivot:
                idx += 1
                arr[idx], arr[i] = arr[i], arr[idx]

        idx += 1
        arr[idx], arr[right] = arr[right], arr[idx]

        return idx

    def quicksort(arr, left, right):
        if left <= right:
            m = partition(arr, left, right)
            quicksort(arr, left, m - 1)
            quicksort(arr, m + 1, right)

        return arr

    quicksort(nums, 0, len(nums) - 1)

    def maxheap(arr, root, max_len):
        left = root * 2 + 1
        right = root * 2 + 2
        maxidx = root

        if left < max_len and arr[maxidx] < arr[left]:
            maxidx = left

        if right < max_len and arr[maxidx] < arr[right]:
            maxidx = right

        if maxidx != root:
            arr[root], arr[maxidx] = arr[maxidx], arr[root]
            maxheap(arr, maxidx, max_len)

        return

    def heapsort(arr):
        n = len(arr)
        for i in range(n-1, -1, -1):
            maxheap(arr, i, n)

        for i in range(n-1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            maxheap(arr, 0, i)

        return arr


    heapsort(nums)
