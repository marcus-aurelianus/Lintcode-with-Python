class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverseBetween(self,head,m,n):
        that_guy,next_guy=head,[]
        guys=[]
        i=1
        while that_guy!=None:
            next_guy=that_guy.next
            guys.append(that_guy)
            if m<i<=n:
                that_guy.next=guys[i-2]
            if i==n:
                guys[m-1].next=next_guy
                guys[m-2].next=guys[n-1]
            that_guy=next_guy
            i+=1

sol=Solution()
# node5=ListNode(5)
# node4=ListNode(4,node5)
# node3=ListNode(3,node4)
# node2=ListNode(2,node3)
# node1=ListNode(1,node2)
# kappa=node1
# while(kappa!=None):
#     print(kappa.val)
#     kappa=kappa.next
# sol.reverseBetween(node1,2,4)
# kappa=node1
# while(kappa!=None):
#     print(kappa.val)
#     kappa=kappa.next
node17=ListNode(6062) ##GG,forget to implement a loop here...So stewpid
node16=ListNode(3403,node17)
node15=ListNode(2270,node16)
node14=ListNode(1007,node15)
node13=ListNode(56,node14)
node12=ListNode(5792,node13)
node11=ListNode(5040,node12)
node10=ListNode(8488,node11)
node9=ListNode(8879,node10)
node8=ListNode(8560,node9)
node7=ListNode(4421,node8)
node6=ListNode(5069,node7)
node5=ListNode(3904,node6)
node4=ListNode(7595,node5)
node3=ListNode(2881,node4)
node2=ListNode(3760,node3)
sol.reverseBetween(node2,2,7)
kappa=node2
while(kappa!=None):
    print(kappa.val)
    kappa=kappa.next

