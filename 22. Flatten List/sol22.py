class Solution:
    def flatten(self,nestedList):
        result = []
        sta = list()
        for ele in reversed(nestedList):
            sta.append(ele)
        while len(sta) > 0:
            ele = sta[-1]
            sta.pop()
            if isinstance(ele, int):
                result.append(ele)
            else:
                for sub_ele in reversed(ele):
                    sta.append(sub_ele)
        return result                  
#Test Cases:  
sol=Solution()
a=[-68,[[-97,-66],85,81,[[-63],[-71]],[-97,[166]]],[[35,136],[[125],[104]],[134,71],[154,[29]],32],[[[-2],31],164,139,[-52,[15]],[-53,25]],[-71,[[66],[139]],155,[[102],[-44]],[156,17]],[[29,-30],75,[-92,14],[1,159],76],[[133,[43]],[[-88],128],139,2,[182,[-45]]],52,[[[197],[151]],[[58],131],[[-21],[144]],[[-97],108],[147,[147]]],[[[180],[-1]],[129,[67]],[-20,-42],179,-83]]
print(sol.flatten(a))
