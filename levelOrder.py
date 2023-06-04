
def levelOrder(root):
    if root is None:
        return None

    que = []
    que.append(root)
    rst = []
    while len(que) > 0:
        tmp = []
        cnt = len(que)
        while cnt > 0:
            cur = que.pop(0)
            tmp.append(cur.val)
            if cur.left is not None:
                que.append(cur.left)
            if cur.right is not None:
                que.append(cur.right)
            cnt -= 1
        rst.append(tmp)

    return rst
