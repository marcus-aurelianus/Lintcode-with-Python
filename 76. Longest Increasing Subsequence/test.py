class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def CeilIndex(self,A, l, r, key): 
      
        while (r - l > 1): 
          
            m = l + (r - l)//2
            if (A[m] >= key): 
                r = m 
            else: 
                l = m 
        return r 
   
    def longestIncreasingSubsequence(self,nums): 
      
        # Add boundary case, 
        # when array size is one 
        n = len(nums)
        tailTable = [0 for i in range(n + 1)] 
        point = 0 # always points empty slot 
       
        tailTable[0] = nums[0] 
        point = 1
        for i in range(1, n): 
            print(nums[i],point)
            if (nums[i] < tailTable[0]): 
      
                # new smallest value 
                tailTable[0] = nums[i] 
       
            elif (nums[i] > tailTable[point-1]): 
      
                # A[i] wants to extend 
                # largest subsequence 
                tailTable[point] = nums[i] 
                point+= 1
       
            else: 
                # A[i] wants to be current 
                # end candidate of an existing 
                # subsequence. It will replace 
                # ceil value in tailTable 
                tailTable[self.CeilIndex(tailTable, -1, point-1, nums[i])] = nums[i] 
            print(tailTable)
       
        return point
  
    
sol=Solution()
lst=[ 2, 5, 3, 7, 11, 8, 10, 13,3,4,5,6,7,8,9,1,10] 
print(sol.longestIncreasingSubsequence(lst))

