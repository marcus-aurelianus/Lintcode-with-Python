class Interval:
    def __init__(self,start,end):
        self.start=start
        self.end=end
class Solution:
    def insert(self,intervals,newInterval):
        res,temp=[],[]
        for interval in intervals:
            if interval.end==newInterval.start:
                temp.append(interval.start)
                temp.append(newInterval.end)
            elif interval.start==newInterval.end:
                if temp:
                    temp.pop()
                    temp.append(interval.end)
                else:
                    temp.append(newInterval.start)
                    temp.append(interval.end)
            else:
                if temp:
                    res.append(Interval(temp[0],[1]))
                    temp=[]
                else:
                    if interval.start>newInterval.end:
                        res.append(newInterval)
                    res.append(interval)
        if temp:
            res.append(Interval(temp[0],[1]))
        return res
#Test Case
interval_a=Interval(1,2)
interval_b=Interval(5,9)
intervals=(interval_a,interval_b)
sol=Solution()
new=Interval(3,4)
c=sol.insert(intervals,new)
print(c)
for k in c:
    print(k.start,k.end)
