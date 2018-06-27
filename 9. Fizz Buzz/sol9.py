class Solution:
    def fizzBuzz(self,n):
        res=[]
        for i in range(1,n+1):
            if i%15==0:
                res.append("fizz buzz")
            elif i%5==0:
                res.append("buzz")
            elif i%3==0:
                res.append("fizz")
            else:
                res.append(str(i))
        return res


#Test Cases:
    
sol=Solution()
print(sol.fizzBuzz(15))
