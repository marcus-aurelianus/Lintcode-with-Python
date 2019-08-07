class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverse(self,head):
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current= next
        return prev
      

            
# Test Case：
sol=Solution()
node3=ListNode(3)
node2=ListNode(2,node3)
node1=ListNode(1,node2)
kappa=node1
while(kappa!=None):
    print(kappa.val)
    kappa=kappa.next
sol.reverse(node1)
kappa=node3
while(kappa!=None):
    print(kappa.val)
    kappa=kappa.next
