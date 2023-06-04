def merge(intervals):
    itvl_sort = sorted(intervals, key=lambda x: x[0])
    new_arr = []
    new_arr.append(itvl_sort[0])
    n = len(intervals)
    idx = 0
    for i in range(1, n):
        t1 = new_arr[idx]
        t2 = itvl_sort[i]

        if t2[0] >= t1[0] and t2[0] <= t1[1]:
            new_1 = min(t1[0], t2[0])
            new_2 = max(t1[1], t2[1])
            new_arr[idx] = [new_1, new_2]
        else:
            new_arr.append(t2)
            idx += 1

    return new_arr


intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]
print(merge(intervals))
