class Solution:
    def diceSum(self,n):
        base_case={0:1}
        for i in range(1,n+1):
            temp={}
            for key1 in base_case:
                for key2 in range(1,7):
                    val=base_case[key1]*(1/6)
                    ori=temp.get(key1+key2,0)
                    temp[key1+key2]=ori+val
            base_case=temp
        return list(map(lambda x:list(x),base_case.items()))
#Test Cases:  
sol=Solution()
print(sol.diceSum(3))
