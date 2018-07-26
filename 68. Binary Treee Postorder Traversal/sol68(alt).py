
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if root is None:
            return
        result=[]
        stk = []
        node=root
        while stk or node:
            while node:
                stk.append(node)
                node=node.left if node.left else node.right
            node=stk.pop()
            result.append(node.val)
            if stk and stk[-1].left==node:
                node=stk[-1].right
            else:
                node=None
        return result
node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
sol=Solution()
print(sol.postorderTraversal(node1))
