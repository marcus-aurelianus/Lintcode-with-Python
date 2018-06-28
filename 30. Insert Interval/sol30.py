class Interval:
    def __init__(self,start,end):
        self.start=start
        self.end=end
class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results = []
        insertPos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                results.append(interval)
                insertPos += 1
            elif interval.start > newInterval.end:
                results.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        results.insert(insertPos, newInterval)
        return results
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
