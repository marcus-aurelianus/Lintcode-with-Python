class Solution:
    def minWindow(self,source,target):
        outputStr = ''
        if not source or not target:
            return outputStr
        end = 0
        currHash,targetHash={},{}
        for char in target:
            targetHash[char] = targetHash.get(char,0) + 1
        n, miniLen =len(source), len(source)+1
        Tlen, Mlen = len(targetHash), 0
        for start in range(n):
            while end < n and Mlen < Tlen:
                char = source[end]
                if char in targetHash:
                    currHash[char]=currHash.get(char,0) + 1
                    if targetHash[char]==currHash[char]:
                        Mlen+=1
                end += 1
            if Mlen == Tlen and end - start < miniLen:
                miniLen = end - start
                outputStr = source[start:end]
            char = source[start]
            if char in targetHash:
                if targetHash[char] == currHash[char]:
                    Mlen -= 1
                currHash[char]-=1
        return outputStr
                    
                
                    

#Test Case
source='absdfaadbabab'
target="adb"
sol=Solution()
print(sol.minWindow(source,target))
