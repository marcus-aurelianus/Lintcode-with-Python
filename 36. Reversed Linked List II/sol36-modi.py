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
            current = next
        return prev
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        if m == 1:
            i = 0
            temp = head
            prev = None
            current = head
            while (True):
                if current is None:
                    return prev
                if i == n:
                    temp.next=current
                    return prev
                next = current.next
                current.next = prev
                prev = current
                current = next
                i += 1      
        else:
            temp = head
            start = head
            for i in range(1,m-1):
                start = start.next
            end = start.next
            for i in range(m,n):
                end = end.next
            prev = start.next
            current = end.next
            for i in range(m,n+1):
                prev_next = prev.next
                prev.next = current
                current = prev
                prev = prev_next
                print(current.val,"that guy")
                temp1=temp
##                print("##trial##")
##                while(temp1):
##                    print(temp1.val)
##                    temp1=temp1.next
            start.next=end
            return temp
# Test Case：
sol=Solution()
node6=ListNode(6)
node5=ListNode(5,node6)
node4=ListNode(4,node5)
node3=ListNode(3,node4)
node2=ListNode(2,node3)
node1=ListNode(1,node2)
kappa=node1
while(kappa):
    print(kappa.val)
    kappa=kappa.next
kappa=sol.reverseBetween(node1,2,5)
print("###")
while(kappa):
    print(kappa.val)
    kappa=kappa.next
#print(node4.next.val)
