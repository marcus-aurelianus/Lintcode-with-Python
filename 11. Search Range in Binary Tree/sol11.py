class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left,self.right=None,None
class Solution:
    def srarchRange(self,root,k1,k2):
        if root==None:
            return ""
        queue=[root]
        answer=[]
        while queue:
            node=queue.pop(0)
            if node!=None:
                if k1<=int(node.val)<=k2:
                    answer.append(int(node.val))
                queue.append(node.left)
                queue.append(node.right)
        answer.sort()
        return answer
    def deserialize(self, data):
        # write your code here
        if data == "{}":
            return None
        data = data[1:-1].split(',')
        root = TreeNode(data[0])
        queue = []
        queue.append(root)
        index = 0
        isLeft = True
        for i in range(1, len(data)):
            if data[i] != '#':
                node = TreeNode(data[i])
                if isLeft:
                    queue[index].left = node
                else:
                    queue[index].right = node 
                queue.append(node)
            if isLeft == False:
                index += 1
            isLeft = not isLeft
        return root
#Test Cases:
    
sol=Solution()
tree=sol.deserialize("{20,8,22,4,12}")
print(sol.srarchRange(tree,10,22))

