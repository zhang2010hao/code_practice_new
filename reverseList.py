
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def reverseList(head):
#     root = ListNode(-1)
#     nodes = []
#
#     while head is not None:
#         nodes.append(head)
#         head = head.next
#
#     cur = root
#     while len(nodes) > 0:
#         tmp = nodes.pop(-1)
#         tmp.next = None
#         cur.next = tmp
#         cur = cur.next
#
#     return root.next

def reverseList(head):
    def dfs(cur):
        if cur is None or cur.next is None:
            return cur

        newhead = dfs(cur.next)

        cur.next.next = cur # 此时cur的next指向原来的cur.next， 而newhead也是指向cur.next, 因此这个代码可以将newhead的next指向cur
        cur.next = None # 上一步完成反转后，cur.next还是原来的，所以需要将cur.next置为空

        return newhead

    newhead = dfs(head)

    return newhead

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l3.next = l2
l2.next = l1

rst = reverseList(l3)
print()

