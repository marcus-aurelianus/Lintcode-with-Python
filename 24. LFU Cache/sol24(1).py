from collections import OrderedDict
class LFUCache:
    
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.c2n = {}
        self.minCount = None
        
    def set(self,key,value):
        if self.capacity > 0:
            if key in self.cache:
                self.cache[key][0] = value
                self.get(key)
                return

            if len(self.cache) == self.capacity:
                n = self.c2n[self.minCount].popitem(last=False)
                del self.cache[n[0]]

            c2n_temp=self.c2n.get(1,OrderedDict())
            c2n_temp[key]=value
            self.c2n[1]= c2n_temp
            self.cache[key] = [value,1]
            self.minCount = 1
            
        
    def get(self,key):

        if key not in self.cache:
            return -1

        value,cache_count = self.cache[key]
        del self.c2n[cache_count][key]  


        if not self.c2n[cache_count]:
            del self.c2n[cache_count]

        cache_count+=1
        c2n_temp=self.c2n.get(cache_count,OrderedDict())
        c2n_temp[key]=value
        self.c2n[cache_count]= c2n_temp
        self.cache[key][1]+=1

        if not self.c2n.get(self.minCount,None):
            self.minCount+=1
        return value

    
sam=LFUCache(3)

def set(a,b):
    sam.set(a,b)
def get(a):
    b=sam.get(a)
    print(a,b)

set(2, 2)
set(1, 1)
get(2)
get(1)
get(2)
set(3, 3)
set(4, 4)
get(3)
get(2)
get(1)
get(4)    
