

def processTasks(tasks):
    import heapq

    tasks.append([10 ** 9 + 1, 10 ** 9 + 1, 1])  # 加个哨兵
    res, q = 0, []
    for [s, e, p] in sorted(tasks, key=lambda x: x[0]):
        while q and q[0][0] + res < s:
            if q[0][0] + res >= q[0][1]:
                heapq.heappop(q)  # 任务早已完成，移除
            else:
                res += min(q[0][1], s) - (q[0][0] + res)
        heapq.heappush(q, [e - p + 1 - res, e + 1])
    return res


tasks = [[1,3,2],[2,5,3],[5,6,2]]
rst = processTasks(tasks)
print(rst)