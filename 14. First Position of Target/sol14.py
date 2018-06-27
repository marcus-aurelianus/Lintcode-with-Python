class Solution:
    def binarySearch(self,num,target):
        left,right=0,len(num)-1
        while(left<=right):
            if left!=right:
                mid=(left+right)//2  
                if target>num[right] or target<num[left]:
                    return -1
                elif num[mid]<target:
                    left,right=mid+1,right
                else:
                    left,right=left,mid-1
            else:
                return left



#Test Cases:
    
sol=Solution()
print(sol.binarySearch([1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,4,5,10],4))
