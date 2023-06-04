
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if len(lists) == 0:
        return None

    n = len(lists)
    root = ListNode(val=-10000000)
    cur = root
    while True:
        min_v = 10000000
        flag = False
        min_idx = -1
        for i in range(n):
            if lists[i] is not None:
                if lists[i].val < min_v:
                    min_v = lists[i].val
                    min_idx = i
                    flag = True
        if flag:
            cur.next = ListNode(val=min_v)
            cur = cur.next

            tmp_node = lists[min_idx].next
            lists[min_idx] = tmp_node
        else:
            break

    return root.next


