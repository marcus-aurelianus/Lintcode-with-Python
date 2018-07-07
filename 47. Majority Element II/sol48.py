class Solution:
    def majorityNumber(self,nums):
        res=[None,None]
        count=[0,0]
        for num in nums:
            if res[0]==num:
                count[0]+=1
            elif res[1]==num:
                count[1]+=1
            elif count[0]==0:
                count[0]+=1
                res[0]=num
            elif count[1]==0:
                count[1]+=1
                res[1]=num
            else:
                count[0]-=1
                count[1]-=1
        print(res,count)
        count=[0,0]
        for num in nums:
            if num==res[0]:
                count[0]+=1
            elif num==res[1]:
                count[1]+=1
        return res[0] if count[0]>count[1] else res[1]

#Test Case:
sol=Solution()
lst=[1,1,1,1,2,3,4,5,6,7,8,9]
print(sol.majorityNumber(lst))
