class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[right] + numbers[left]
            if sum == target:
                return [left+1, right+1]
            if sum > target:
                right -= 1
            if sum < target:
                left += 1
        return
        
