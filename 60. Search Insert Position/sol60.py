class Solution:
    def SearchInsert(self,A,target):
        start,end=0,len(A)-1
        while start<end-1:
            mid=(start+end)//2
            if A[mid]>target:
                end=mid
            else:
                start=mid
        if target>A[end]:
            return end+1
        elif target>A[start]:
            return end
        else:
            return start
#Test Case:
sol=Solution()
print(sol.SearchInsert([1,3,5,6],3))
