class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count,i=0,1
        while (5**i<n):
            count+=n//5**i
            i+=1
        return count


#Test Cases:
    
sol=Solution()
print(sol.trailingZeros(1001171717))
