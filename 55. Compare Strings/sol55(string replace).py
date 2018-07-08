class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        for b in B:
            if b not in A:
                return False
            else:
                A = A.replace(b, '', 1)
        return True
#Test Case:
sol=Solution()
c1="ABCD"
c2="ABD"
print(sol.compareStrings(c1,c2))
#print(c1,c2)
            
