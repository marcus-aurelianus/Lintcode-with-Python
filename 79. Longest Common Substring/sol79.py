class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        m,n=len(A),len(B)
        res=[]
        for i in range(m+1):
            temp=[0]*(n+1)
            res.append(temp)
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    res[i][j]=0
                elif A[i-1] == B[j-1]:
                    res[i][j]=res[i-1][j-1]+1
                else:
                    res[i][j]=min(res[i-1][j],res[i][j-1])
        out=0
        for res_1 in res:
            out=max(out,max(res_1)) 
        return out
sol=Solution()
a="acb"
b="ac"
print(sol.longestCommonSubstring(a,b))
