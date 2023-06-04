class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    fast = head
    slow = head
    pre = head

    if head is None or head.next is None:
        return None

    flag = False
    i = 0
    while fast is not None and fast.next is not None and slow is not None:
        if i == 0:
            fast = fast.next.next
            slow = slow.next
            i += 1
        else:
            if fast == slow:
                flag = True
                break
            else:
                fast = fast.next.next
                slow = slow.next

    if flag:
        while True:
            if pre == slow:
                return pre
            else:
                pre = pre.next
                slow = slow.next
    else:
        return None

l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2

print(detectCycle(l1))
