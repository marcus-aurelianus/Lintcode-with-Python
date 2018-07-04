class Solution:
    """ 
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        chars.sort(key=lambda c: c.isupper())
#Test Case:
sol=Solution()
char=list('abAcD')
sol.sortLetters(char)
print(char)
