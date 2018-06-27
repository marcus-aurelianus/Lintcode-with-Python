class Solution:
    def permute(self,nums):
        n=len(nums)
        res,temp,mirrors,temp_m=[],[],[],[]
        if nums:
            for i in range(n):
                res.append([nums[i]])
                mirrors.append([i])
            while(len(res[0])<n):
                for j in range(len(mirrors)):
                    for i in range(n):
                        if i not in mirrors[j]:
                            if len(res[0])==n-1:
                                permu=res[j]+[nums[i],]
                                if permu not in temp:
                                    temp.append(permu)
                            else:
                                temp_m.append(mirrors[j]+[i,])
                                temp.append(res[j]+[nums[i],])
                res,temp,mirrors,temp_m=temp,[],temp_m,[]
            return res,mirrors
        return [[]]
#Test Cases:  
sol=Solution()
print(sol.permute([1,2,2,3]))
