class Solution:
    def majorityNumber(self,nums):
        res=None
        count=0
        for num in nums:
            if count==0:
                res=num
                count+=1
            elif res==num:
                count+=1
            else:
                count-=1
        return res

#Test Case:
sol=Solution()
lst=[1,1,1,1,1,2,2,2,2,3]
print(sol.majorityNumber(lst))
