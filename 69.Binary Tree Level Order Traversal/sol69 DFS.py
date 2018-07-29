class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        stk=[]

        if root is None:
            return stk

        q=[root]
        
        depth=0

        self.DFS(root,stk,depth)
        return stk

    def DFS(self,root,stack,depth):
        if root is None:
            return
        if depth>len(stack)-1:
            stack.append([])
        stack[depth].append(root.val)
        depth+=1
        self.DFS(root.left,stack,depth)
        self.DFS(root.right,stack,depth)
        



node1=TreeNode(3)
node2=TreeNode(9)
node3=TreeNode(20)
node4=TreeNode(15)
node5=TreeNode(7)
node1.left=node2
node1.right=node3
node3.left=node4
node3.right=node5

print(Solution().levelOrder(node1))
    
