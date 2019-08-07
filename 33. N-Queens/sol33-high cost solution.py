class Solution:
    def solveNQueens(self,n):
        sol=[[],]*n
        i=0
        for i in range(n):
            next_sol=[]
            for ans in sol:
                j=0
                while j<n:
                    if self.is_valid(ans,[i,j]):
                        temp=ans.copy()
                        temp.append([i,j])
                        if temp not in next_sol:
                            next_sol.append(temp)
                    j+=1          
            sol=next_sol
            i+=1
        return self.draw(sol,n)
    def is_valid(self,lsts,test):
        for lst in lsts:
            if abs(lst[0]-test[0])==abs(lst[1]-test[1]) or lst[0]==test[0] or lst[1]==test[1]:
                return False
        return True
    def draw(self,subSet,n):
        out=[]
        for eles in subSet:
            temp=[]
            for ele in eles:
                temp+=["."*ele[1]+"Q"+"."*(n-1-ele[1])]
            out.append(tem
sol=Solution()
print(sol.solveNQueens(4))
