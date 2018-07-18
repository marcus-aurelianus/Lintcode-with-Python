class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        for i in range(n):
            A[i+m] = B[i]
        A.sort()

#Test Case:
sol=Solution()
A=[9,10,11,12,13,0,0,0,0]
B=[4,5,6,7]
print(sol.mergeSortedArray(A,len(A)-len(B),B,len(B)))
print(A,B)
