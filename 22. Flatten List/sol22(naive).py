class Solution:
    def flatten(self,nestedList):
        res,temp1,temp2=[],[],[]
        i,j=0,0
        if type(nestedList)==int:
            res.append(nestedList)
        else:
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
                                temp2=(temp1[j+1:]+temp2)
                                temp1=temp1[j]
                                j=0
                        else:
                            temp1,temp2=temp2,[]
                            j=0
                    j=0
                    temp1,temp2=[],[]
                i+=1
        return res                   
#Test Cases:  
sol=Solution()
a=[-68,[[-97,-66],85,81,[[-63],[-71]],[-97,[166]]],[[35,136],[[125],[104]],[134,71],[154,[29]],32],[[[-2],31],164,139,[-52,[15]],[-53,25]],[-71,[[66],[139]],155,[[102],[-44]],[156,17]],[[29,-30],75,[-92,14],[1,159],76],[[133,[43]],[[-88],128],139,2,[182,[-45]]],52,[[[197],[151]],[[58],131],[[-21],[144]],[[-97],108],[147,[147]]],[[[180],[-1]],[129,[67]],[-20,-42],179,-83]]
print(sol.flatten(a))
