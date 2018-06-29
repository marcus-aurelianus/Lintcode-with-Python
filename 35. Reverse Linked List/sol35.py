class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverse(self,head):
        that_guy,next_guy=head,[]
        guys=[]
        i=-1
        while that_guy!=None:
            next_guy=that_guy.next
            guys.append(that_guy)
            that_guy.next=guys[i] if i!=-1 else None
            that_guy=next_guy
            i+=1

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
