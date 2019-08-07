class Solution:
    def fourSum(self,numbers,target):
        numbers.sort()
        out=[]
        i=0
        while (i<len(numbers)-3):
            if numbers[i]!=numbers[i-1] or i==0:
                sols=self.threeSum(numbers[i+1:],target-numbers[i])
                if sols:
                    for sol in sols:
                        temp=[numbers[i]]+sol
                        if temp not in out:
                            out.append(temp)
            i+=1
        return out

    def threeSum(self,numbers,target):
        numbers.sort()
        out=[]
        i=0
        while (i<len(numbers)-2):
            if numbers[i]!=numbers[i-1] or i==0:
                sols=self.twoSum(numbers[i+1:],target-numbers[i])
                if sols:
                    for sol in sols:
                        sam=[numbers[i]]+sol
                        if sam not in out:
                            out.append(sam)
            i+=1
        return out

    def twoSum(self,number,target):
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
lst=[1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,0,0,-2,2,-5,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99]
print(sol.fourSum(lst,11))
