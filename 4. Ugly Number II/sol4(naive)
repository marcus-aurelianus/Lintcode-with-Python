class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description
    """
    def nthUglyNumber(self,n):
        res=[1]
        i=2
        def helper(num):
            if num==1:
                return True
            else:
                if num%2==0:
                    return helper(num//2)
                if num%3==0:
                    return helper(num//3)
                if num%5==0:
                    return helper(num//5)
                else:
                    return False
        while len(res)<n:
            if helper(i):
                res.append(i)
            i+=1
        return res[-1]
#Test Cases:
    
sol=Solution()
print(sol.nthUglyNumber(1000))
