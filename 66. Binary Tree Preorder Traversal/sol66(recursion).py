class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if root==None:
            return []
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
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
print(sol.preorderTraversal(node1))
