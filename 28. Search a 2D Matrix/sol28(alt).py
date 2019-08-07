class Solution:
    def searchMatrix(self,matrix,target):
        if matrix==None or len(matrix)==0:
            return False          
        n,m=len(matrix),len(matrix[0])
        x,y,pos=0,m-1,-1
        while x<=n-1 and y>=0:
            goal=matrix[x][y]
            if target>goal:
                x+=1
            if target<goal:
                pos=x
                break
            if target==goal:
                return True
        if pos>=0:
            x,y=0,m-1
            if matrix[pos][0]== target:
                return True
            while x<=y:
                mid=(x+y)//2
                if matrix[pos][mid]==target:
                    return True
                elif matrix[pos][mid]>target:
                    x,y=x,mid-1
                else:
                    x,y=mid+1,y
        return False
            
sol=Solution()
a=[[1,5,8,12,13,15,18,20,25,26,28,33,38,40,43,49,52,53,59],[84,100,110,129,141,156,177,198,220,242,254,266,284,297,316,326,343,358,373],[388,398,419,439,449,460,472,495,516,539,560,582,600,610,624,643,668,691,710],[720,733,751,765,787,804,814,832,856,880,905,930,950,974,999,1012,1022,1039,1061],[1081,1091,1102,1126,1151,1175,1194,1219,1239,1253,1263,1274,1287,1298,1308,1318,1337,1361,1382],[1404,1417,1437,1452,1466,1487,1503,1518,1537,1555,1578,1590,1601,1613,1636,1659,1669,1688,1712]]
print(sol.searchMatrix(a,1888))
