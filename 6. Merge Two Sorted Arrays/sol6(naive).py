class Solution:
    def mergeSortedArray(self,A,B):
        res=[]
        while(A and B):
            if A[0]<=B[0]:
                res.append(A[0])
                A.pop(0)
            else:
                res.append(B[0])
                B.pop(0)
        while(A):
            res.append(A[0])
            A.pop(0)
        while(B):
            res.append(B[0])
            B.pop(0)
        return res

#Test Cases:
    
sol=Solution()
print(sol.mergeSortedArray([1,2,3,4],[2,4,5,6]))
