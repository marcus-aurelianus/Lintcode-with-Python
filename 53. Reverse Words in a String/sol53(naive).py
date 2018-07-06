class Solution:
    def reverseWords(self,s):
        res,temp="",""
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if temp!="":
                    temp+=s[i]
                    res+=temp
                    temp=""
            else:
                temp=s[i]+temp
        res+=temp
        return res

#Test Case:
sol=Solution()
string=""
print(sol.reverseWords(string))
