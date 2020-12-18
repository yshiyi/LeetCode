'''
189. Rotate Array
Array

Description:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Similar Questions:
Rotate List - Medium
Reverse Words in a String II - Medium
'''

# Solution:
'''
        Method 1: Brute force 1
                  Move the last element to the front one by one
                  Will exceed the time limit when the len(nums) is large
        '''
        if len(nums) < 2:
            return nums
        for i in range(k):
            last = nums[-1]
            for j in range(len(nums)-1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = last
            
        '''
        Method 2: Brute force 2
                  switch the adjacent elements until the last element moves to the front
                  Will exceed the time limit when the len(nums) is large
        '''
        if len(nums) < 2:
            return nums
        for i in range(k):
            for j in range(len(nums)-1, 0, -1):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
        
        '''
        Method 3: Create an extra array
                  Let k = len(nums) % k, just in case of k > len(nums)
                  Runtime: about 40 - 48 ms; Memory: 13.7 - 13.9 MB
        '''
        k %= len(nums)
        if len(nums) < 2 or k == 0:
            return nums
        nums[:] = nums[-k:] + nums[:len(nums)-k]
        
        '''
        Method 4: Create an extra array
                  Elements will be moved to (i+k)%len(nums) position.
                  Runtime: 36 ms; Memory: 14.8 MB
        '''
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]           
        nums[:] = a
        
        '''
        Method 5: Using reverse
                  At first, we reverse the entire array.
                  Second, we reverse the first k elements.
                  Third, we reverse the rest of n-k elements.
                  Runtime: 68 -76 ms; Memory: 13.7 - 13.8 MB
        '''
        n = len(nums)
        k %= n
        
        self.reverse(nums, 0, n - 1)
        print(nums)
        self.reverse(nums, 0, k - 1)
        print(nums)
        self.reverse(nums, k, n - 1)
        print(nums)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        


