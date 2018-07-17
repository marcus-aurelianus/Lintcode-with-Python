class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        l, h = 0, len(A) - 1
        while (l <= h):
            m = ((h + l) >> 1)
            print(l,m,h)
            if A[m] == target:
                return True
            elif (A[m] >= A[l] and target <= A[m] and target >= A[l]) or (A[m] < A[l] and not(target <= A[h] and target >= A[m]) or (A[m]==A[h]==A[h-1])):
                h = m - 1
            else:
                l = m + 1
        return False
#Test Case:
sol=Solution()
print(sol.search([9,5,6,7,8,9,9,9,9,9,9],8))
