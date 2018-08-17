
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root_val=postorder[-1]
        root=TreeNode(root_val)
        print(inorder,postorder)
        pos=inorder.index(root_val)
        root.left=self.buildTree(inorder[:pos], postorder[:pos])
        root.right=self.buildTree(inorder[pos+1:], postorder[pos:-1])
        return root
        
print(Solution().buildTree([1,2,3],[1,3,2]))
