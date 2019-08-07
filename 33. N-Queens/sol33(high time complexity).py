class Solution:
    def solveNQueens(self,n):
        sol=[[],]*n
        def helper(lsts,test):
            for lst in lsts:
                if abs(lst[0]-test[0])==abs(lst[1]-test[1]) or lst[0]==test[0] or lst[1]==test[1]:
                    return False
            return True
        i=0
        while (i<n):
            next_sol=[]    
            for ans in sol:
                for j in range(n):
                    if helper(ans,[i,j]):
                        temp=ans.copy()
                        temp.append([i,j])
                        if temp not in next_sol:
                            next_sol.append(temp)
            sol=next_sol
            i+=1
        out=[]
        for eles in sol:
            temp=[]
            for ele in eles:
                temp+=["."*ele[1]+"Q"+"."*(n-1-ele[1])]
            out.append(temp)
        return  out
sol=Solution()
print(sol.solveNQueens(4))
