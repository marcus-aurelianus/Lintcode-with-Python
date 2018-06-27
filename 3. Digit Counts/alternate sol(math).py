class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        def helper(k,n):
            if k==0 and n==0:
                return 1
            res=0
            while n!=0:
                res+=(n%10==k)
                n//=10
            return res
        d=n//10
        u=n%10
        if k!=0:
            if n<1:
                return 0
        else:
            if n<10:
                return 1
        if u==9:
            temp=self.digitCounts(k,d)
            return temp*10+d+1 if k!=0 else (temp-1)*10+d+1
        return self.digitCounts(k,n-(u+1))+helper(k,d)*(u+1)+(u>k-1)

#Test Cases:
    
sol=Solution()
print(sol.digitCounts(2,19))
