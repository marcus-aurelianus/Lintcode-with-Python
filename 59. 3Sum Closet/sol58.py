class Solution:
    def threeSumClosest(self,numbers,target):
        numbers.sort()
        out=None
        diff = None
        for i in range (len(numbers)-2):
            curr_diff,sum_up=self.twoSum(numbers[i+1:],target,numbers[i],diff)
            if out is None or curr_diff<diff:
                out = sum_up
                diff = curr_diff
        return out

    def twoSum(self,numbers,target,curr,diff):
        left,right=0,len(numbers)-1
        curr_sum=numbers[left]+numbers[right]
        print(numbers)
        while left<right:
            if diff is None or abs(numbers[left]+numbers[right]+curr-target)<diff:
                diff=abs(numbers[left]+numbers[right]+curr-target)
                curr_sum=numbers[left]+numbers[right]+curr
            if numbers[left]+numbers[right]+curr>target:
                right-=1
            else:
                left+=1
        return diff,curr_sum

#Test Case:
sol=Solution()
lst=[-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5]
print(sol.threeSumClosest(lst,77))
