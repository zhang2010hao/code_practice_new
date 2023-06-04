
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    # que = []
    # root = ListNode(-1)
    # root.next = head
    # cur = root
    # tmp = None
    # i = 0
    # while cur is not None:
    #     if i == left - 1:
    #         tmp = cur
    #
    #     if i >= left and i < right:
    #         que.append(cur)
    #     elif i == right:
    #         cur_next = cur.next
    #         tmp.next = cur
    #         tmp = tmp.next
    #         while len(que) > 0:
    #             tmp.next = que.pop(-1)
    #             tmp = tmp.next
    #         tmp.next = cur_next
    #     elif i > right:
    #         break
    #
    #     cur = cur.next
    #     i += 1
    #
    # return root.next

    root = ListNode(-1)
    root.next = head
    pre = root
    for i in range(left-1):
        pre = pre.next

    cur = pre.next
    for i in range(left, right):
        next = cur.next
        cur.next = next.next
        next.next = pre.next
        pre.next = next

    return root.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

rst = reverseBetween(l1, 2, 5)
print()