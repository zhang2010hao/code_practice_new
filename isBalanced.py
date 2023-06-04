
def isBalanced(root):
    def dfs(cur_node):
        if len(flag) > 0:
            return 0

        if cur_node is None:
            return 0

        left_cnt = dfs(cur_node.left) + 1
        right_cnt = dfs(cur_node.right) + 1

        if abs(right_cnt - left_cnt) > 1:
            flag.append(0)

        return max(left_cnt, right_cnt)

    flag = []
    dfs(root)

    return len(flag) < 1