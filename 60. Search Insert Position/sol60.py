class Solution:
    def SearchInsert(self,A,target):
        start,end=0,len(A)-1
        while start<=end:
            if A[start]==target:
                return start
            elif A[end]==target:
                return end
            else:
                start+=1
                end-=1
        return 0
#Test Case:
sol=Solution()
print(sol.SearchInsert([1,3,5,6],6))
