class Solution:
    def searchMatrix(self,matrix,target):
        left,right=0,len(matrix)-1
        while(left<right):
            if matrix[left][0]>target or matrix[right][-1]<target:
                return False
            elif right-left==1:
                if target>matrix[left][-1]:
                    pos=right
                    break
                elif target<matrix[left][-1]:
                    pos=left
                    break
                else:
                    return True
            else:
                mid=(left+right)//2
                if matrix[mid][0]>target:
                    left,right=left,mid
                elif matrix[mid][0]<target:
                    left,right=mid,right
                else:
                    return True
        left,right=0,len(matrix[pos])-1
        while (left<=right):
            if left==right:
                if matrix[pos][left]==target:
                    return True
                else:
                    return False
            else:
                mid=(left+right)//2
                if matrix[pos][mid]>target:
                    left,right=left,mid-1
                elif matrix[pos][mid]<target:
                    left,right=mid+1,right
                else:
                    return True
#Test Cases:  
sol=Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],24))
