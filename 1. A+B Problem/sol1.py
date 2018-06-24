def Add(x,y):
    while(y!=0 and x!=0):
        if y<0:
            if x>0:
                x,y=x^(-y),-((~x) & (-y))<<1
            else:
                x,y=-(-x^-y),-(-x&-y)<<1
        else:
            if x<0:
                y,x=y^(-x),-((~y) & (-x))<<1
            else:
                x,y=x^y,(x&y)<<1
        print(x,y)
    return x if y==0 else y
#test case: 
#print((0xFFFFFFFF+2)*2) 
#print(Add(-32,33)) 
print(Add(-0xFFFFFFFF+1,0xFFFFFFFF+2))
print(Add(-100,-300))

MAX_BIT = 2**32
MAX_BIT_COMPLIMENT = -2**32

def aplusb(a, b):

    while b != 0:
        if b == MAX_BIT:
            return a ^ MAX_BIT_COMPLIMENT
        carry = a & b
        a = a ^ b
        b = carry << 1

        print(a,b)

    return a
#print(aplusb(0xFFFFFFFF+1,0xFFFFFFFF+1))
#print(0xFFFFFFFF+1+0xFFFFFFFF+1)
