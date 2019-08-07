class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        m,n=len(A),len(B)
        res=[]
        for i in range(m+1):
            temp=[0]*(n+1)
            res.append(temp)
        for i in range(m+1):
            for j in range(n+1):
##                print(A[i],B[j])
##                print(res)
                if i==0 or j==0:
                    res[i][j]=0
                elif A[i-1] == B[j-1]:
                    res[i][j]=res[i-1][j-1]+1
                else:
                    res[i][j]=max(res[i-1][j],res[i][j-1])
        return res[m][n]


sol=Solution()
a="eeeebbceeaebcedaeabbdeebacccadcdbddcdbacacdceeadabacedbbcaab"
b="eaeeaddbbcbcacadbdbdcaaaeabcdbaeacbdeedecceedcaddcbdbdaeabdd"
print(sol.longestCommonSubsequence(a,b))
