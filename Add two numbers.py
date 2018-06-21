def Add(x,y):
    INT_RANGE=0xFFFFFFFF
    while(y!=0):
        x,y=x^y,(x&y)<<1
        x&=INT_RANGE
        print(x,y)
    return x if x>>31 <=0 else x^~INT_RANGE
print(0xFFFFFFFF+2)
print(Add(0xFFFFFFFF+1,0xFFFFFFFF+2))
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
print(aplusb(-100,2000))
