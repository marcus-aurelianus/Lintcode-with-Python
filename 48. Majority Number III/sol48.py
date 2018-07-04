class Solution:
    def majorityNumber(self,nums,k):
        res={}
        freq=0
        for num in nums:
            res[num]=res.get(num,0)+1
            if res[num]>freq:
                freq=res[num]
                out=num
        return out



#Test Case:
sol=Solution()
lst=[3,1,2,3,3,4,4,4]
print(sol.majorityNumber(lst,3))
