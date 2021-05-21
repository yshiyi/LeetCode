class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums)%k != 0:
            return False
        target = sum(nums)/k
        used = [0]*len(nums)
        
        def backtrack(nums, start, k, bucket_sum, used, target):
            if k==0:
                return True
            if bucket_sum == target:
                return backtrack(nums, 0, k-1, 0, used, target)
            for i in range(start, len(nums)):
                if used[i]==1:
                    continue
                if bucket_sum + nums[i] > target:
                    continue
                bucket_sum += nums[i]
                used[i] = 1
                if backtrack(nums, i+1, k, bucket_sum, used, target):
                    return True
                used[i] = 0
                bucket_sum -= nums[i]
            return False
        
        return backtrack(nums, 0, k, 0, used, target)
