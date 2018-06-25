class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        count=0
        dic1={}
        def helper(str1,n):
            if str1 in dic1:
                return dic1[str1]
            else:
                if len(str1)>1:
                    dic1[str1]=helper(str1[0],n)+helper(str1[1:],n)
                    return dic1[str1]
                else:
                    dic1[str1]=str1[0].count(str(n))
                    return dic1[str1]
        for i in range(n+1):
            count+=helper(str(i),k)
            print(dic1)
        return count

#Test Cases:
    
sol=Solution()
print(sol.digitCounts(1, 122))
