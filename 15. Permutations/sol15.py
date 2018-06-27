class Solution:
    def permute(self,nums):
        n=len(nums)
        res,temp=[],[]
        if nums:
            for num in nums:
                res.append([num])
            while(len(res[0])<n):
                for re in res:
                    for num in nums:
                        if num not in re:
                            temp.append(re+[num,])
                res,temp=temp,[]
            return res
        return [[]]
#Test Cases:  
sol=Solution()
print(sol.permute([1,2,3]))
