class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head):
    root = ListNode(val=-5001)

    cur = head

    while cur is not None:
        new_cur = root
        node = ListNode(val=cur.val)
        flag = True
        while new_cur.next is not None:
            if cur.val <= new_cur.next.val:
                new_next = new_cur.next
                new_cur.next = node
                node.next = new_next
                flag = False
                break
            else:
                new_cur = new_cur.next

        if flag:
            new_cur.next = node

        cur = cur.next

    return root.next


n1 = ListNode(val=4)
n2 = ListNode(val=2)
n3 = ListNode(val=1)
n4 = ListNode(val=3)
n1.next = n2
n2.next = n3
n3.next = n4

rest = insertionSortList(n1)
print('')
