
def inorderTraversal(root):
    def dfs(cur):
        if cur is None:
            return

        dfs(cur.left)
        rst.append(cur.val)
        dfs(cur.right)

    if root is None:
        return []

    rst = []
    dfs(root)

    return rst