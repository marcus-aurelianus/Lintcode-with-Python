class Solution:
    def reverseInteger(self,number):
        return int("".join(list(reversed(str(number)))))

#Test Case:
sol=Solution()
print(sol.reverseInteger(900))
