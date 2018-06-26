class Solution:
    """
    @param: : k & A a integer and array
    @return ans a integer
    """
    def kthLargestElement(self,k,A):
        n=len(A)
        def helper(start,end):
            temp1,temp2=start+1,end
            while(temp1<=temp2):
                if A[temp1]>A[start]:
                    temp1+=1
                else:
                    if A[temp1]<A[temp2]:
                        A[temp1],A[temp2]=A[temp2],A[temp1]
                    temp2-=1
                print(A)
            print(A,temp2)
            A[start],A[temp2]=A[temp2],A[start]
            if temp2==k-1:
                return A[temp2]
            elif temp2<k-1:
                return helper(temp2+1,end)
            else:
                return helper(start,temp2-1)  
        return helper(0,n-1)
#Test Cases:
    
sol=Solution()
a=[5,8,5,6,8,4,2,7,9,5,1,3,6,8,7,1,5,9,6,9,8,5]
b=[10,4,7,6,9,3,3,3,1]
print(sol.kthLargestElement(4,b))

print(b)
