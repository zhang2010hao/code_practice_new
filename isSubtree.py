class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot):
    def dfs(cur, arr):
        if cur is None:
            arr.append('null')
            return

        arr.append(cur.val)
        dfs(cur.left, arr)
        dfs(cur.right, arr)

        return

    arr1 = []
    dfs(root, arr1)
    arr2 = []
    dfs(subRoot, arr2)

    n1 = len(arr1)
    n2 = len(arr2)
    i = 0

    while i <= n1 - n2:
        if arr1[i] == arr2[0]:
            flag = True
            for j in range(n2):
                if arr1[i + j] != arr2[j]:
                    flag = False
                    break
            if flag:
                return True

        i += 1

    return False

n1 = TreeNode(3)
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(1)
n5 = TreeNode(2)

n6 = TreeNode(4)
n7 = TreeNode(1)
n8 = TreeNode(2)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

n6.left = n7
n6.right = n8

print(isSubtree(n1, n6))