"""
494. Target Sum

Description:
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' 
before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to 
build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

Follow up:
string = "1111", target = 0
11 - 11 = 0
-11 + 11 = 0
"""
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.total = sum(nums)
        self.dic = [collections.defaultdict(int) for _ in range(len(nums))]
        return self.helper(nums, 0, 0, target)
    
    def helper(self, nums, start, Sum, target):
        if start==len(nums):
            if Sum==target:
                return 1
            else:
                return 0
        
        if Sum+self.total in self.dic[start]:
            return self.dic[start][Sum+self.total]
        
        add = self.helper(nums, start+1, Sum-nums[start], target)
        subtract = self.helper(nums, start+1, Sum+nums[start], target)
        self.dic[start][Sum+self.total]=add+subtract
        return self.dic[start][Sum+self.total]

       

"""
Follow up:
string = "1111", target = 0
"""
class Solution(object):
    def targetSum(self, string, target):
        self.ans = []
        self.helper(string, 0, 0, target, "")
        return self.ans
    
    def helper(self, string, start, Sum, target, s):
        if start==len(string):
            if Sum==target:
                self.ans.append(copy.deepcopy(s))
            return
        for i in range(start, len(string)):
            new_s = string[start:i+1]
            if i==0:
                s += new_s
            else:
                s += "+"+new_s
            self.helper(string, i+1, Sum+int(new_s), target, s)
            if i==0:
                s = s[:-len(new_s)]
            else:
                s = s[:-len(new_s)-1]
            
            s += "-"+new_s
            self.helper(string, i+1, Sum-int(new_s), target, s)
            s = s[:-len(new_s)-1]
