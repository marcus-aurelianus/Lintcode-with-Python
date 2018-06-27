class MinStack:
    def __init__(self):
        self.stk=[]
        self.mins=[]
    def push(self,number):
        self.stk.append(number)
        if self.mins==[] or self.mins[-1]>number:
            self.mins.append(number)
    def pop(self):
        if self.stk[-1]==self.mins[-1]:
            self.mins.pop()
        return self.stk.pop()
    def min(self):
        return self.mins[-1]
#Test Cases:
    
sol=MinStack()
sol.push(1)
print(sol.pop())
sol.push(2)
sol.push(3)
print(sol.min())
sol.push(1)
print(sol.min())


sol1=MinStack()
sol1.push(4)
sol1.push(3)
sol1.push(2)
print(sol1.pop())
print(sol1.min())
