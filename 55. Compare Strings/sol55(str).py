class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        if len(B) == 0:
            return True
        if len(A) == 0:
            return False
        trackTable = [0 for _ in range(26)]
        for i in A:
            trackTable[ord(i) - 65] += 1
        for i in B:
            if trackTable[ord(i) - 65] == 0:
                return False
            else:
                trackTable[ord(i) -65] -= 1
        return True



#Test Case:
sol=Solution()
c1="ABCD"
c2="ABD"
print(sol.compareStrings(c1,c2))
