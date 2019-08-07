class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        tableA={}
        tableB={}
        self.count(tableA,A)
        self.count(tableB,B)
        return tableA == tableB
    def count(self,table,char):
        for i in char:
            freq=table.get(i,0)+1
            table[i]=freq

sol=Solution()
A="abcd"
B="bcad"
print(sol.Permutation(A,B))
