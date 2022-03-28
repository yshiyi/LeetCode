'''
215M.Kth Largest Element in an Array

Description:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

Similar Questions:
Wiggle Sort II - Medium
Top K Frequent Elements - Medium
Third Maximum Number - Easy
Kth Largest Element in a Stream - Easy
K Closest Points to Origin - Medium
Find the Kth Largest Integer in the Array - Medium
Find Subsequence of Length K With the Largest Sum - Easy
K Highest Ranked Items Within a Price Range - Medium
'''

# Solution: Heap
class Solution(object):
    def findKthLargest(self, nums, k):
        q = []
        heapq.heapify(q)
        for num in nums:
            heapq.heappush(q, num)
            if len(q)>k:
                heapq.heappop(q)
        return q[0]

# Solution
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, left, right):
            pivot_index = randint(left, right)
            pivot = nums[pivot_index]
            i = right
            for j in range(right, left-1, -1):
                if nums[j]>=pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    if j==pivot_index:
                        pivot_index = i
                    i -= 1
            i += 1
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            return i
        def quickSelect(nums, left, right, k):
            if left<=right:
                index = partition(nums, left, right)
                if right - index == k - 1:
                    return nums[index]
                if right - index > k - 1:
                    return quickSelect(nums, index+1, right, k)
                else:
                    return quickSelect(nums, left, index-1, k-(right-index+1))
            return -1
        
        
        return quickSelect(nums, 0, len(nums)-1, k)
