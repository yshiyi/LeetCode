* [Two Sum](#two-sum)
* [Longest Repeated Subarray](#Longest-Repeated-Subarray)
* [29. Divide Two Integers](#29-Divide-Two-Integers)
* [Simplified XML Validator](#Simplified-XML-Validator)
* [66. Plus One](#66-Plus-One)
* [238. Product of Array Except Self](#238-Product-of-Array-Except-Self)
* [146. LRU Cache](#146-LRU-Cache)
* [69. Sqrt(x)](#69-sqrtx)
* [13. Roman to Integer](#13-Roman-to-Integer)
* [Knapsack](#Knapsack)
* [208. Implement Trie (Prefix Tree)](#208-Implement-Trie-Prefix-Tree)


# Two Sum
Output all possible solutions.\
Example:\
Input: \[4,4,4,1,1\], target = 5\
Output: \[4,1\], \[4,1\], \[4,1\], \[4,1\], \[4,1\], \[4,1\]\
**Method:**\
Notice, there are duplicate solutions. Therefore, we need to use Counter to count all the appearances of each element.\
Then use two pointer to sweep the keys from the two ends.
```
import collections
class Solution(object):
    def twoSum(self, nums, target):
        count = collections.Counter(nums)
        vals = list(count.keys())
        vals.sort()
        p1, p2 = 0, len(vals)-1
        ans = []
        while p1 < p2:
            _sum = vals[p1] + vals[p2]
            if _sum==target:
                for _ in range(count[vals[p1]]*count[vals[p2]]):
                    ans.append([vals[p1], vals[p2]])
                p2 -= 1
            elif _sum > target:
                p2 -= 1
            else:
                p1 += 1
        return ans
```


# Longest Repeated Subarray
Example:\
Input: \[2,2,2,2,2,1,1,4,4\]\
Output: \[2,2,2,2,2\]\

# 29. Divide Two Integers

# Simplified XML Validator

# 66. Plus One

# 238. Product of Array Except Self

# 146. LRU Cache

# 69. Sqrt(x)

# 13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.\
Symbol       Value\
I             1\
V             5\
X             10\
L             50\
C             100\
D             500\
M             1000\
Example:\
Input: s = "MCMXCIV"\
Output: 1994\
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.\
**Method:**\
In most of cases, the string is in non-ascending order.\
We only need to find the letters that are smaller than its next one.\
Time complexity: O(N)\
Space complexity: O(1)\
```
class Solution(object):
    def romanToInt(self, s):
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s)==1:
            return dic[s[0]]
        ans = 0
        i = 0
        while i < len(s)-1:
            if dic[s[i]]>=dic[s[i+1]]:
                ans += dic[s[i]]
                i += 1
            else:
                ans += dic[s[i+1]] - dic[s[i]]
                i += 2
        if i == len(s)-1:
            ans += dic[s[i]]
        return ans
```

# Knapsack
给你⼀个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。其中第 i 个物品的重量为 wt\[i\]，价值为 val[i]，现在让你⽤这个背包装物品，最多能装的价值是多少？\
Example:\
N = 3, W = 4\
wt = \[2, 1, 3\]\
val = \[4, 2, 3\]\
**Method:**\
This is a dynamic programming problem.\
First, we need to determine the states and actions.\
There are two states: the number of objects, and weight remain in the bagpack.\
Two actions: put object i into the bag, and not put object i into the bag.\

Second, we need to define a transition function.\
The optimal value in each state dp\[n\]\[w\] should be the maximum of outcome of two actions.\
1. If we put the object n into the bag, what is the optimal value?
   val\[n-1\] + dp\[n-1\]\[w-wt\[n-1\]\], object n's value + the optimal value that put n-1 objects with w-wt[n-1] weight\
2. If we don't put th object n into the bag.
   dp\[n-1\]\[w\], the optimal value that put n-1 objects with w weight\
3. Corner case. if w-wt\[n-1\]<0.
   It means we can't put object n into the bag, the dp\[n\]\[w\] = dp\[n-1\]\[w\]\
```
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
[[0, 0, 0, 0, 0], 
 [0, 0, 4, 4, 4], 
 [0, 2, 4, 6, 6], 
 [0, 2, 4, 6, 6]]
```

# 208. Implement Trie (Prefix Tree)
