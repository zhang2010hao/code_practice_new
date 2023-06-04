class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    def dfs(cur):
        if cur.left is not None:
            node2root[cur.left] = cur
            dfs(cur.left)

        if cur.right is not None:
            node2root[cur.right] = cur
            dfs(cur.right)

    node2root = {root: None}
    dfs(root)

    p_parents = set([p.val])
    while p in node2root:
        if node2root[p] is not None:
            p_parents.add(node2root[p].val)
            p = node2root[p]
        else:
            break

    if q.val in p_parents:
        return q
    while q in node2root:
        if node2root[q].val in p_parents:
            return node2root[q]
        else:
            q = node2root[q]

    return None


n1 = TreeNode(val=3)
n2 = TreeNode(val=9)
n3 = TreeNode(val=20)
n4 = TreeNode(val=15)
n5 = TreeNode(val=7)
n6 = TreeNode(val=10)
n7 = TreeNode(val=11)

n1.left = n2
n1.right = n3
n2.left = n6
n2.right = n7
n3.left = n4
n3.right = n5

rest = lowestCommonAncestor(n1, n2, n5)
print()
