class Solution:
    def searchMatrix(self,matrix,target):
        if matrix==[] or matrix[0]==[]:
            return 0      
        n,m=len(matrix),len(matrix[0])
        x,y,count=0,m-1,0
        while x<n and y>=0:
            goal=matrix[x][y]
            if target==goal:
                count+=1
                x+=1
                y-=1
            elif target<goal:
                y-=1
            else:
                x+=1
        return count

#Test Case:
sol=Solution()
mat=[[1,3,5,7],[2,4,7,8],[3,5,9,10]]
print(sol.searchMatrix(mat,3))
