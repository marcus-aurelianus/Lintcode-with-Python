class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        lst=list(A)
        for ele in B:
            if ele not in lst:
                return False
            else:
                lst.remove(ele)
        return True
#Test Case:
sol=Solution()
c1="ABCD"
c2="ABD"
print(sol.compareStrings(c1,c2))
            
