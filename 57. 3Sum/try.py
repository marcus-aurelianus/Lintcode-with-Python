class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self,numbers):
        numbers.sort()
        out=[]
        for i in range (len(numbers)):
            temp=numbers[i+1:]
            sols=self.twoSum(temp,-numbers[i])
            if sols:
                for sol in sols:
                    sam=[numbers[i]]+sol
                    sam.sort()
                    if sam not in out:
                        out.append(sam)
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
                        
            
