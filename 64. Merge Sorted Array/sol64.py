class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        i,j,pos=m-1,n-1,m+n-1
        while (i>=0 and j>=0):
            if i>=0 and A[i]>B[j]:
                A[pos],A[i]=A[i],A[pos]
                i-=1
            else:
                A[pos]=B[j]
                j-=1
            pos-=1
        while j>=0:
            A[pos]=B[j]
            pos-=1
            j-=1

#Test Case:
sol=Solution()
A=[9,10,11,12,13,0,0,0,0]
B=[4,5,6,7]
print(sol.mergeSortedArray(A,len(A)-len(B),B,len(B)))
print(A,B)
