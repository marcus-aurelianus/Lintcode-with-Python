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
        
        while q!=[]:
            new_q = []
            stk.append([n.val for n in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q=new_q
        return stk




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
