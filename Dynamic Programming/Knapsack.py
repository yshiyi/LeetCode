"""
给你⼀个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。其中第 i 个物品的重量为
wt[i]，价值为 val[i]，现在让你⽤这个背包装物品，最多能装的价值是多少？

Example:
N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
"""

"""
This is a dynamic programming problem.
First, we need to determine the states and actions.
There are two states: the number of objects, and weight remain in the bagpack.
Two actions: put object i into the bag, and not put object i into the bag.

Second, we need to define a transition function.
The optimal value in each state dp[n][w] should be the maximum of outcome of two actions.
1. If we put the object n into the bag, what is the optimal value?
   val[n-1] + dp[n-1][w-wt[n-1]], object n's value + the optimal value that put n-1 objects with w-wt[n-1] weight
2. If we don't put th object n into the bag.
   dp[n-1][w], the optimal value that put n-1 objects with w weight
3. Corner case. if w-wt[n-1]<0.
   It means we can't put object n into the bag, the dp[n][w] = dp[n-1][w]
"""
class Solution(object):
    def knapSack(self, N, W, wt, val):
        dp = [[0] * (W+1) for _ in range(N+1)]
        for n in range(1, N+1):
            for w in range(1, W+1):
                if w - wt[n-1] < 0:
                    dp[n][w] = dp[n-1][w]
                else:
                    dp[n][w] = max(dp[n-1][w], val[n-1] + dp[n-1][w-wt[n-1]])
        return dp[N][W]

sol = Solution()
N, W = 3, 4
wt = [2, 1, 3]
val = [4, 2, 3]
print(sol.knapSack(N, W, wt, val))
"""
[[0, 0, 0, 0, 0], 
 [0, 0, 4, 4, 4], 
 [0, 2, 4, 6, 6], 
 [0, 2, 4, 6, 6]]
"""
