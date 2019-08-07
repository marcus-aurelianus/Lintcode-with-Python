class Solution:
    def totalNQueens(self,n):
        if n<=0:
            return
        res=[0]
        self.dfs(n,[],res)
        return res[0]
    
    def dfs(self,n,subSet,res):
        if len(subSet)==n:
            res[0]+=1
        for column in range(n):
            if not self.check(subSet,column):
                continue
            subSet.append(column)
            self.dfs(n,subSet,res)
            subSet.pop()
            
    def check(self,subSet,test):
        n=len(subSet)
        for order in range(n):
            if subSet[order]==test or abs(subSet[order]-test)==abs(order-n):
                return False
        return True
sol=Solution()
print(sol.totalNQueens(7))
