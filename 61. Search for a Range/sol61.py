class Solution:
    def searchRange(self, A, target):
        if len(A) == 0:
            return [-1, -1]
        
        start1, end1 = 0, len(A) - 1
        start2, end2 = 0, len(A) - 1
        while start1 < end1-1 or start2<end2-1:
            mid1=(start1+end1)//2
            mid2=(start2+end2)//2
            if A[mid2]>target:
                end2=mid2
            else:
                start2=mid2
            if A[mid1]>=target:
                end1=mid1
            else:
                start1=mid1
        print(start1,end1,start2,end2)
        if [start1,end1]==[start2,end2]:
            if A[end1]==target:
                return [end1,end1]
            else:
                return [-1,-1]
        elif A[end1]==target:
            if A[end2]==target:
                return [end1,end2]
            else:
                return [end1,start2]
        else:
            return [-1,-1]

#Test Case:
sol=Solution()
print(sol.searchRange([5,5,5,5,5,5,5,5,5,5],5))
