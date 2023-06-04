class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    n = 0
    cur = headA
    while cur:
        n += 1
        cur = cur.next

    m = 0
    cur = headB
    while cur:
        m += 1
        cur = cur.next

    if n > m:
        r = 0
        while r < n - m:
            headA = headA.next
            r += 1
    elif m > n:
        r = 0
        while r < m - n:
            headB = headB.next
            r += 1

    while headA is not None and headB is not None and headA != headB:
        headA = headA.next
        headB = headB.next

    return headA


# listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
l1 = ListNode(x=4)
l2 = ListNode(x=1)
l3 = ListNode(x=8)
l4 = ListNode(x=4)
l5 = ListNode(x=5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

l6 = ListNode(x=5)
l7 = ListNode(x=6)
l8 = ListNode(x=1)

l6.next = l7
l7.next = l8
l8.next = l3
rst = getIntersectionNode(l1, l6)
print()