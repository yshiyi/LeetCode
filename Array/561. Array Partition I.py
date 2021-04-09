class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort();
        sum = 0
        for i in range(1, len(nums), 2):
            sum += min(nums[i], nums[i-1])
        return sum
