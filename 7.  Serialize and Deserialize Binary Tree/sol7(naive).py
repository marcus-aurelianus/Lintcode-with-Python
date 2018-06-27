"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if root == None:
            return "{}"
        queue = [root]
        answer = []
        while queue:
            node = queue.pop(0)
            answer.append(node)
                
            if node != None:
                queue.append(node.left)
                queue.append(node.right)
        queue = answer
        # construct string
        str = ""
        for x in range(len(queue)):
            str += "#" if queue[x] is None else "{}".format(queue[x].val)
            if x != len(queue) - 1: 
                str += ","
        return "{" + str + "}"
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
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

tree=sol.deserialize("{3,9,20,#,#,15,7}")
print(sol.serialize(tree))
