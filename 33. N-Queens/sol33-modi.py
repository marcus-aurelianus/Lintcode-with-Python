class Solution:
    def solveNQueens(self,n):
        if n<=0:
            return
        res=[]
        self.dfs(n,[],res)
        return res
    def dfs(self,n,subSet,res):
        if len(subSet)==n:
            res.append(self.draw(subSet))
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
    def draw(self, subSet):
        out = []
        for i in range(len(subSet)):
            temp = ['.'] * len(subSet)
            temp[subSet[i]] = 'Q'
            out.append(''.join(temp))
        return out       
sol=Solution()
pattern=sol.solveNQueens(4)
print(pattern)
##for p in pattern:
##    for row in p:
##        print(row)
##    print("------")
