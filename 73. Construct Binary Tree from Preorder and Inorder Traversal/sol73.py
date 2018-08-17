
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
    def buildTree(self, preorder, inorder):
        if not inorder or not preorder:
            return None
        root_val=inorder[0]
        root=TreeNode(root_val)
        pos=inorder.index(root_val)
        print(preorder[0:pos+1],preorder[pos+1:])
        root.left=self.buildTree(preorder[1:pos+1],inorder[:pos])
        root.right=self.buildTree( preorder[pos+1:],inorder[pos+1:])
        return root
        
print(Solution().buildTree([2,1,3],[1,2,3]))
