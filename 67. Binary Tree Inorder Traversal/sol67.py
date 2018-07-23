"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        stack=[]
        result=[]
        while stack:
            stack.append(root)
            root=root.left
        while stack:
            node=stack[-1]
            result.append(node.val)
            if node.right:
                node=node.right
                while node:
                    stack.append(node)
                    node=node.left
            else:
                node=stack.pop()
                while stack and stack[-1].right==node:
                    node=stack.pop()
        return result
      
