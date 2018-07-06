class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        return ' '.join(reversed(s.strip().split()))
        
        
        
#Test Case:
sol=Solution()
string="what the heck"
print(sol.reverseWords(string))
