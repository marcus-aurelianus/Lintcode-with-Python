class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    """
    f denotes local_max and g denotes global_max.
    local_max[i%2][k] means the maximum value for k subsets in the first i element(Must include Ith element).
    global_max[i%2][k] means the maximum value for k subsets in the first i element(Not nessesary including Ith element).
    local[i%2][k]=max(global[(i-1)%2][k-1], local[(i-1)%2][k]) + nums[i-1]
    global[i%2][k]=max(global[i-1][k],local[i][k])
    """
    def maxSubArray(self, nums, k):
        min_val = float("-inf")
        n = len(nums)
        f = [[min_val] * (k + 1), [min_val] * (k + 1)]
        g = [[min_val] * (k + 1), [min_val] * (k + 1)]
        
        f[0][0] = 0
        g[0][0] = 0
        for i in range(1, n + 1):
            f[i % 2][0] = 0
            g[i % 2][0] = 0
            for j in range(1, k + 1):
                f[i % 2][j] = max(f[(i - 1) % 2][j] + nums[i - 1],
                                  g[(i - 1) % 2][j - 1] + nums[i - 1])
                g[i % 2][j] = max(g[(i - 1) % 2][j], f[i % 2][j])
        #print(i,f,g)
        return g[n % 2][k]
#Test Case:
sol=Solution()
lst=[4, 1, 1, -1, -3, -5, 6, 2, -6, -2,-3,-4,-5,-6]
for i in range(14):
    print(sol.maxSubArray(lst,i))
