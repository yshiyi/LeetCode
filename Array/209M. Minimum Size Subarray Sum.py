class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = float('inf')
        if nums[0]>=target:
            return 1
        left, right, ans = 0, 1, nums[0]
        while right < len(nums):
            ans += nums[right]
            while(ans >= target):
                min_len = min(min_len, right - left + 1)
                ans -= nums[left]
                left += 1
            right += 1
        if min_len==float('inf'):
            return 0
        else:
            return min_len
        
