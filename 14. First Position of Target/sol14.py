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
                    left,right=left,mid
            else:
                if num[left]==target:
                    return left
                return -1



#Test Cases:
    
sol=Solution()
print(sol.binarySearch([4,5,9,9,12,13,14,15,15,18],10))
