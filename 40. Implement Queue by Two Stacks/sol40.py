class MyQueue:
    
    def __init__(self):
        self.stk1=[]
        self.stk2=[]
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.stk1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        if self.stk2==[]:
            while self.stk1!=[]:
                ele=self.stk1.pop()
                self.stk2.append(ele)
        return self.stk2.pop()
    """
    @return: An integer
    """
    def top(self):
        if self.stk2==[]:
            while self.stk1!=[]:
                ele=self.stk1.pop()
                self.stk2.append(ele)
        return self.stk2[-1]


# Test case:
sol=MyQueue()
sol.push(1)
print(sol.pop())

