
def findKthNumber(n, k):
    def stepnums(cur):
        step_n, step_tmp, first, last, last_tmp = 0, 0, cur, cur, cur

        while first <= n:
            step_n = step_n + min(n, last) - first + 1
            step_tmp = step_tmp + min(n, last_tmp) - first + 1
            last_tmp = first * 10 + 9
            last = last * 10 + 9
            first = first * 10

        return step_n



    cur = 1
    k = k - 1 # 因为cur已经设置初始值，所以k需要先减去1
    while k > 0:
        # 获得当前值下的字典数节点数，包含当前节点在内
        step_nums = stepnums(cur)

        if step_nums <= k:
            # 字典树的节点数不大于K值说明第个值在下面的节点中，先从下个节点开始
            cur = cur + 1
            k = k - step_nums
        else:
            # 字典树的节点数大于k，说明第k个值在本数中，由于需要往下层节点走，所以cur需要更新，k对应的要扣除掉当前的节点
            cur = cur * 10
            k = k - 1

    return cur

    # num_str = [str(i) for i in range(1, n + 1)]
    # sorted_num_str = sorted(num_str)
    #
    # return int(sorted_num_str[k - 1])

rst = findKthNumber(10001, 10000)
print(rst)
