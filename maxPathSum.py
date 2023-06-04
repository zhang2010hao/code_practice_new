class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    def dfs(cur):
        if cur is not None:
            cur_v = cur.val
            left_v, right_v = 0, 0
            if cur.left is not None:
                left_v = dfs(cur.left)

            if cur.right is not None:
                right_v = dfs(cur.right)

            max_v = max(cur_v, cur_v + left_v, cur_v + right_v, cur_v + left_v + right_v)
            if len(max_sum) == 0:
                max_sum.append(max_v)

            if max_v > max_sum[0]:
                max_sum[0] = max_v

            return max(cur_v, cur_v + left_v, cur_v + right_v)

        else:
            return 0

    max_sum = []
    dfs(root)

    return max_sum[0]

n1 = TreeNode(5)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(maxPathSum(n1))