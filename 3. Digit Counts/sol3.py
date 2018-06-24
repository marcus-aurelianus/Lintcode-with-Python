class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        count=0
        for i in range(k):
            count+=str(k).count(str(n))
        return count

Test Cases:
    
sol=Solution()
print(sol.trailingZeros(1001171717))
