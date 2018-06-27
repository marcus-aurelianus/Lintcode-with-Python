class Solution:
    def flatten(self,nestedList):
        res,temp1,temp2=[],[],[]
        i,j=0,0
        while i <len(nestedList):
            if type(nestedList[i])==int:
                res.append(nestedList[i])
            else:
                temp1=nestedList[i]
                while j<len(temp1) or temp2!=[]:
                    if j<len(temp1):
                        if type(temp1[j])==int:
                            res.append(temp1[j])
                            j+=1
                        else:
                            temp2.extend(temp1[j+1:])
                            temp1=temp1[j]
                            j=0
                    else:
                        temp1,temp2=temp2,[]
                        j=0
                j=0
            i+=1
        return res                   
#Test Cases:  
sol=Solution()
print(sol.flatten([1,[2,[3,6,7,8,89,3],5,6,[8,9,[8,9],9]],[1,2]]))
