class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n=len(A)+len(B)
        if n%2==1:
            return self.findMedian(A,B,n//2+1)
        else:
            smaller=self.findMedian(A,B,n//2)
            larger=self.findMedian(A,B,n//2+1)
            return (smaller+larger)/2
    def findMedian(self,A,B,pos):
        if len(A)==0:
            return B[pos-1]
        if len(B)==0:
            return A[pos-1]
        if pos==1:
            return min(A[0],B[0])
        a=A[pos//2-1] if len(A)>=pos//2 else None
        b=B[pos//2-1] if len(B)>=pos//2 else None

        if b is None or (a is not None and a<b):
            return self.findMedian(A[pos//2:],B,pos-pos//2)
        return self.findMedian(A,B[pos//2:],pos-pos//2)


#Test Case:
sol=Solution()
A=[1,2,3,4,5,6]
B=[2,3,4,5]
print(sol.findMedianSortedArrays(A,B))
