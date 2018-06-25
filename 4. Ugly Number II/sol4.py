class Solution:
    """
    @param n: An integer
    @return: the nth ugly number as description
    """
    def nthUglyNumber(self,n):
        last=[0,0,0]
        temp=[1,1,1]
        mat=[2,3,5]
        res=[1]
        while len(res)<n:
            for i in range(3):
                while(res[last[i]]*mat[i])<=res[-1]:
                    last[i]+=1
            for i in range(3):
                temp[i]=res[last[i]]*mat[i]
            num=min(temp)
            res.append(num)
        return res[-1]
#Test Cases:
    
sol=Solution()
print(sol.nthUglyNumber(1000))
