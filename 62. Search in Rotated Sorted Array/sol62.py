class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        l, h = 0, len(A) - 1
        while (l <= h):
            m = ((h + l) >> 1)
            if A[m] == target:
                return m
            elif (A[m] > A[l] and target < A[m] and target >= A[l]) or (A[m] < A[l] and not (target <= A[h] and target > A[m])):
                h = m - 1
            else:
                l = m + 1
        return -1
#Test Case:
sol=Solution()
print(sol.search([1001,10001,10007,1,10,101,201],1001))
