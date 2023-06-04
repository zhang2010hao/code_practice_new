
def mergeTwoLists(list1, list2):
    head = ListNode(-1)
    cur = head

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next

        cur = cur.next

    if list1 is not None:
        cur.next = list1
    else:
        cur.next = list2

    return head.next