# 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
def bubblesort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
# 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 重复第二步，直到所有元素均排序完毕。
def selectionsort(arr):
    # 选择排序
    n = len(arr)
    for i in range(n - 1):
        minv_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[minv_idx]:
                minv_idx = j

        if minv_idx != i:
            arr[i], arr[minv_idx] = arr[minv_idx], arr[i]

    return arr


# 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
# 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
def insertionsort(arr):
    for i in range(len(arr)):
        preidx = i - 1
        cur = arr[i]
        while preidx >= 0 and arr[preidx] > cur:
            arr[preidx + 1] = arr[preidx]
            preidx -= 1

        arr[preidx + 1] = cur

    return arr


def shellSort(arr):
    import math
    gap = 1
    while (gap < len(arr) / 3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = math.floor(gap / 3)
    return arr


# 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
# 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
# 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
# 重复步骤 3 直到某一指针达到序列尾；
# 将另一序列剩下的所有元素直接复制到合并序列尾。
def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))


def merge(left, right):
    rst = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            rst.append(left.pop(0))
        else:
            rst.append(right.pop(0))

    if len(left) > 0:
        rst.extend(left)

    if len(right) > 0:
        rst.extend(right)

    return rst


# 从数列中挑出一个元素，称为 “基准”（pivot）；
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


def quicksort(arr, left, right):
    if left < right:
        m = partition(arr, left, right)
        quicksort(arr, left, m - 1)
        quicksort(arr, m + 1, right)

    return arr



def heap_max(arr, root, arr_len):
    # https://blog.csdn.net/m0_70372647/article/details/124870580
    # 大顶堆（小顶堆）是一种完全二叉树结构，由大顶堆（小顶堆）构成的数组中，假设父节点的索引是i，则左子结点的索引为2*i+1， 右子节点索引为2*i+2
    left, right = 2 * root + 1, 2 * root + 2
    larger = root
    if left < arr_len and arr[left] > arr[larger]:
        larger = left
    if right < arr_len and arr[right] > arr[larger]:
        larger = right

    if root != larger:
        arr[root], arr[larger] = arr[larger], arr[root]
        heap_max(arr, larger, arr_len)

    else:
        return


def heapsort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        heap_max(arr, i, n)

    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap_max(arr, 0, i)

    return arr


nums = [5, 1, 1, 2, 0, 0]
print(heapsort(nums))
print(quicksort(nums, 0, len(nums) - 1))
print(mergesort(nums))
print(insertionsort(nums))
print(selectionsort(nums))
print(bubblesort(nums))


def countingSort(arr, maxValue):
    bucketLen = maxValue + 1
    bucket = [0] * bucketLen
    sortedIndex = 0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr


def bucket_sort(s):
    """桶排序"""
    min_num = min(s)
    max_num = max(s)
    # 桶的大小
    bucket_range = (max_num - min_num) / len(s)
    # 桶数组
    count_list = [[] for i in range(len(s) + 1)]
    # 向桶数组填数
    for i in s:
        count_list[int((i - min_num) // bucket_range)].append(i)
    s.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            s.append(j)


def RadixSort(list):
    i = 0  # 初始为个位排序
    n = 1  # 最小的位数置为1（包含0）
    max_num = max(list)  # 得到带排序数组中最大数
    while max_num > 10 ** n:  # 得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}  # 用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])  # 将每个桶置空
        for x in list:  # 对每一位进行排序
            radix = int((x / (10 ** i)) % 10)  # 得到每位的基数
            bucket[radix].append(x)  # 将对应的数

        # 组元素加入到相 应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:  # 若桶不为空
                for y in bucket[k]:  # 将该桶中每个元素
                    list[j] = y  # 放回到数组中
                    j += 1
        i += 1

    return list

# if __name__ == '__main__':
#     a = [3.2,6,8,4,2,6,7,3]
#     bucket_sort(a)
#     print(a) # [2, 3, 3.2, 4, 6, 6, 7, 8]
