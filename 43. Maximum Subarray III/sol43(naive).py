class Solution:
    def maxSubArray(self,nums,k):
        def helper(lsts):
            if lsts is None or len(lsts)==0:
                return 0
            n=len(lsts)
            local=max_local=lsts[0]
            for i in range(1,n):
                max_local=lsts[i]+max(0,max_local)
                local=max(local,max_local)
            return local
        def partition(n,div):
            result=[[0]]
            while len(result[0])<=div:
                res=[]
                for ele in result:
                    j=len(ele)
                    if div+1-len(ele)==n-ele[-1]:
                        temp=ele.copy()
                        temp.append(ele[-1]+1)
                        res.append(temp)
                    elif j<div:
                        for i in range(1,n-(div+1-len(ele))+2-(ele[-1])):
                            temp=ele.copy()
                            temp.append(ele[-1]+i)
                            res.append(temp)
                    else:
                        temp=ele.copy()
                        temp.append(n)
                        res.append(temp)
                result=res
            return result 
        n=len(nums)
        parts=partition(n,k)
        def helper2(partition,lsts):
            n=len(partition)
            out=0
            for i in range(1,n):
                out+=helper(lsts[partition[i-1]:partition[i]])
            return out
        largest=[]
        for part in parts:
            if largest==[]:
                largest=helper2(part,nums)
            else:
                largest=max(largest,helper2(part,nums))
        return largest

#Test Case:
sol=Solution()
lst=[-1,4,-2,3,-2,3]
print(sol.maxSubArray(lst,2))
