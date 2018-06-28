class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        m,n=len(s1),len(s2)
        dp_map=[]
        if m+n!=len(s3):
            return False
        for i in range (m+1):
            dp_map.append([False]*(n+1))
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0:
                    dp_map[i][j]=True
                elif i==0 and s2[j-1]==s3[j-1]:
                    dp_map[i][j] = dp_map[i][j-1];
                elif j==0 and  s1[i-1]==s3[i-1]:
                    dp_map[i][j] = dp_map[i-1][j]
                elif s1[i-1]==s3[i+j-1] and s2[j-1]!=s3[i+j-1]:
                    dp_map[i][j] = dp_map[i-1][j]
                elif s1[i-1]!=s3[i+j-1] and s2[j-1]==s3[i+j-1]:
                    dp_map[i][j] = dp_map[i][j-1]
                elif s1[i-1]==s3[i+j-1] and s2[j-1]==s3[i+j-1]:
                    dp_map[i][j]=(dp_map[i-1][j] or dp_map[i][j-1]) 
        return dp_map[m][n]



#Test Case:
sol=Solution()
print(sol.isInterleave('aabcc','dbbca','aadbbcbcac'))
