class Solution:
    def searchMatrix(self,matrix,target):
        if matrix==None or len(matrix)==0:
            return False          
        n,m=len(matrix),len(matrix[0])
        x,y,pos=0,m-1,0
        while x<=n-1 and y>=0:
            goal=matrix[x][y]
            if target>goal:
                x+=1
            if target<goal:
                pos=x
                break
            if target==goal:
                return True
        if pos:
            x,y=0,m-1
            while x<=y:
                if x==y:
                    if matrix[pos][x]==target:
                        return True
                    else:
                        return False
                else:
                    mid=(x+y)//2
                    if matrix[pos][mid]>target:
                        x,y=x,mid-1
                    elif matrix[pos][mid]<target:
                
