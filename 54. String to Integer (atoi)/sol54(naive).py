class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        str=str.strip()
        if str=="":
            return 0
        i = 0
        sign = 1
        res=''
        length = len(str)
        INT_MAX = (1 << 31) - 1
        if str[i]=="+":
            i+=1
        elif str[i]=="-":
            i+=1
            sign=-1
        for i in range(i,length):
            if not str[i].isdigit():
                break
            res+=str[i]
        try:
            out=sign*int(float(res))
        except:
            out=0
        return out if abs(out)<INT_MAX else INT_MAX if out>0 else -(INT_MAX+1)
            
            
#Test Case:
sol=Solution()
string=""
print(sol.atoi(string))
