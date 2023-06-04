class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):
    if not head or not head.next:
        return head  # termination.

    # cut the LinkedList at the mid index.
    slow, fast = head, head.next
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    mid, slow.next = slow.next, None  # save and cut.

    # recursive for cutting.
    left, right = sortList(head), sortList(mid)

    # merge `left` and `right` linked list and return it.
    h = res = ListNode(0)
    while left and right:
        if left.val < right.val:
            h.next, left = left, left.next
        else:
            h.next, right = right, right.next
        h = h.next

    h.next = left if left else right

    return res.next

l1 = ListNode(-1)
l2 = ListNode(5)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(0)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
sortList(l1)
print()

