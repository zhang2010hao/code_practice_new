
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    slow = head
    fast = head.next

    if fast is None or fast.next is None:
        return

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    h2 = slow.next
    slow.next = None
    pre = ListNode(-1)
    pre.next = h2
    while h2.next is not None:
        tmp = h2.next
        h2.next = tmp.next
        tmp.next = pre.next
        pre.next = tmp

    h2 = pre.next

    cur = head.next
    pre = head
    while cur is not None and h2 is not None:
        tmp1 = cur.next
        tmp2 = h2.next
        pre.next = h2
        pre.next.next = cur
        pre = pre.next.next
        cur = tmp1
        h2 = tmp2

    if h2:
        pre.next = h2
    else:
        pre.next = cur



l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
reorderList(l1)
print()


