class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        count=0
        for i in range(n+1):
            count+=str(i).count(str(k))
        return count 


#Test Cases:
    
sol=Solution()
print(sol.digitCounts(1, 11))
