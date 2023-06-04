# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    rest = []
    if root is not None:
        que = [root]
        drc = 1
        while len(que) > 0:
            tmp = []
            new_nodes = []
            if drc == 1:
                while len(que) > 0:
                    node = que.pop(0)
                    tmp.append(node.val)
                    if node.left is not None:
                        new_nodes.append(node.left)
                    if node.right is not None:
                        new_nodes.append(node.right)

                drc = -1
            else:
                while len(que) > 0:
                    node = que.pop(-1)
                    tmp.append(node.val)
                    if node.right is not None:
                        new_nodes.insert(0, node.right)
                    if node.left is not None:
                        new_nodes.insert(0, node.left)

                drc = 1

            rest.append(tmp)
            que = new_nodes

    return rest


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

print(zigzagLevelOrder(n1))
