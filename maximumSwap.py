def maximumSwap(num):
    if num < 12:
        return num

    arr = []
    while num > 9:
        x = num % 10
        num = num // 10
        arr.insert(0, x)
    arr.insert(0, num)

    i = 0
    n = len(arr)
    while i < n - 1:
        if arr[i] == 9:
            i += 1
            continue
        max_num = arr[i + 1]
        pos = i + 1
        for j in range(i+2, n):
            if arr[j] >= max_num:
                max_num = arr[j]
                pos = j

        if max_num > arr[i]:
            arr[pos] = arr[i]
            arr[i] = max_num
            break

        i += 1
    rst = 0
    for i, v in enumerate(arr):
        rst += pow(10, n - 1 - i) * v

    return rst

num = 1000000000
rst = maximumSwap(num)
print(rst)

