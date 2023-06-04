class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k):
    # def reverse(head, tail):
    #     tmp = tail.next
    #     p = head
    #     while tmp != tail:
    #         nex = p.next
    #         p.next = tmp
    #         tmp = p
    #         p = nex
    #
    #     return tail, head
    #
    # hair = ListNode(0)
    # hair.next = head
    # pre = hair
    #
    # while head:
    #     tail = pre
    #     # 查看剩余部分长度是否大于等于 k
    #     for i in range(k):
    #         tail = tail.next
    #         if not tail:
    #             return hair.next
    #     nex = tail.next
    #     head, tail = reverse(head, tail)
    #     # 把子链表重新接回原链表
    #     pre.next = head
    #     tail.next = nex
    #     pre = tail
    #     head = tail.next
    #
    # return hair.next


    # def reverse(head, tail):
    #     tmp = tail.next
    #     p = head
    #     while tmp != tail:
    #         nex = p.next
    #         p.next = tmp
    #         tmp = p
    #         p = nex
    #
    #     return tail, head
    #
    # root = ListNode(0)
    # root.next = head
    # pre = root
    # while head is not None:
    #     tail = pre
    #     for i in range(k):
    #        tail = tail.next
    #        if tail is None:
    #            return root.next
    #
    #     nex = tail.next
    #     head, tail = reverse(head, tail)
    #     pre.next = head
    #     tail.next = nex
    #
    #     pre = tail
    #     head = tail.next
    #
    # return root.next

    if k == 1:
        return head

    root = ListNode(0)
    root.next = head
    pre = root
    cur = pre.next
    while cur:
        tail = cur
        for i in range(k-1):
            tail = tail.next
            if tail is None:
                return root.next

        for i in range(k-1):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        pre = cur
        cur = pre.next


    return root.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
rst = reverseKGroup(l1, 2)
print()
