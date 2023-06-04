def reversePairs(nums):
    def merge_sort(arr):
        if len(arr) < 2:
            return arr

        m = len(arr) // 2
        arr_l = merge_sort(arr[:m])
        arr_r = merge_sort(arr[m:])

        cnt = cnts[0]
        rest = []
        ll = len(arr_l)
        lr = len(arr_r)
        li = 0
        ri = 0
        while li < ll and ri < lr:
            if arr_l[li] <= arr_r[ri]:
                rest.append(arr_l[li])
                li += 1
                cnt += ri
            else:
                rest.append(arr_r[ri])
                ri += 1

        if li < ll:
            rest.extend(arr_l[li:])
            cnt = cnt + ri * (ll - li)
        else:
            rest.extend(arr_r[ri:])

        cnts[0] = cnt

        return rest

    cnts = [0]

    merge_sort(nums)

    return cnts[0]


print(reversePairs([1, 3, 2, 3, 1]))
