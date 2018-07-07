class Solution:
    def previousPermutation(self,nums):
        pos1,n=-1,len(nums)
        for i in range(n-1,-1,-1):
            if nums[i]<=nums[i-1]:
                pos1=i-1
                break
        def rever(lst):
            res=[]
            while lst:
                res.append(lst.pop())
            return res
        if pos1==-1:
            return rever(nums)
        else:
            pos2=pos1+1
            while pos2<n and nums[pos1]>nums[pos2]:
                pos2+=1
            pos2-=1
            temp1,temp2=nums[:pos1]+[nums[pos2],],nums[pos1+1:pos2]+[nums[pos1],]+nums[pos2+1:]
            return temp1+rever(temp2)
        


#Test Case:
sol=Solution()
lst=[4, 0, 7, 1, 2, 3, 8, 9]
lst1=[1,3,2]
print(sol.previousPermutation(lst1))
