class LFUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
    def set(self,key,value):
        if len(self.cache)<self.capacity:
            self.cache[key]=[value,0]
        else:
            items=list(self.cache.items())
            item=min(items,key=lambda x:x[1][1])
            del self.cache[item[0]]
            self.cache[key]=[value,0]
    def get(self,key):
        if key in self.cache:
            self.cache[key][1]+=1
            return self.cache[key][0]
        else:
            return -1
#Test Cases:  
sol=LFUCache(3)
sol.set(2,2)
sol.set(1,1)
print(sol.get(2))
print(sol.get(1))
print(sol.get(2))
sol.set(3,3)
sol.set(4,4)
print(sol.get(3))
print(sol.get(2))
print(sol.get(1))
print(sol.get(4))
