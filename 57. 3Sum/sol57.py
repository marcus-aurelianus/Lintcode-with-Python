class Solution:
    def threeSum(self,numbers):
        out=[]
        for i in range (len(numbers)):
            temp=numbers[:i]+numbers[i+1:]
            sols=self.twoSum(temp,-numbers[i])
            if sols:
                for sol in sols:
                    sam=[numbers[i]]+sol
                    sam.sort()
                    if sam not in out:
                        out.append(sam)
        return out

    def twoSum(self,number,target):
        number.sort()
        left,right=0,len(number)-1
        sol=[]
        while left<right:
            if number[left]+number[right]==target:
                sol.append([number[left],number[right]])
                right-=1
                left+=1
            elif number[left]+number[right]>target:
                right-=1
            else:
                left+=1
        return sol

#Test Case:
sol=Solution()
lst=[-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5]
print(sol.threeSum(lst))
