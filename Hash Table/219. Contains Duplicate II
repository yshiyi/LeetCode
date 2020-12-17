'''
219. Contains Duplicate II
Array, Hash Table, Sliding Window

Description:
Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and 
the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Similar Questions:
Contains Duplicate - Easy
Contains Duplicate III - Medium
'''

# Solution:
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        '''
        Method 1: Create three dictionaries.
                  The 1st one contains the characters have been seen.
                  The 2nd one contains those haven't.
                  The 3rd one contans the difference of the indices of two seen characters.
                  Loop through the list.
                  If the char is not in eith of seen or unseen (first time encounter), we save it and its index to seen.
                  If the char is in unseen and not in seen (second time encounter), we remove it from unseen and save it and its index to seen.
                    In the same time, we save the difference between the current index and the previous index to result.
                  If the char is in seen (encounter it more than twice), compare the value saved in result and the difference between the current index and the previous index in seen.
                    If less than the value saved, update the result.
                  At the end, remember to check the len(result.values()) in case there is no repeated char.
        '''
        seen = {}
        unseen = {}
        result = {}
        if len(nums) < 2:
            return False
        for i in range(len(nums)):
            if nums[i] not in seen and nums[i] not in unseen:
                unseen[nums[i]] = i
            elif nums[i] not in seen and nums[i] in unseen:
                seen[nums[i]] = i
                result[nums[i]] = i - unseen[nums[i]]
                del unseen[nums[i]]
            elif nums[i] in seen:
                if i - seen[nums[i]] < result[nums[i]]:
                    result[nums[i]] = i - seen[nums[i]]
        if len(result.values()) != 0 and min(result.values()) <= k:
            return True
        else:
            return False
        
        
        """
        Method 2: Using sliding window,
                  Make a sliding window with size k, and check if there is any duplicates in the window.
                  If the length of the window exceeds k, then remove the first number in the window.
        """
        Set = set()  # Create a sliding window
        
        for i,num in enumerate(nums):
            if num in Set: # if already seen in last k items, then return True
                return True
            else: # otherwise, add that num to the set
                Set.add(num)
            
            if len(Set) > k: # there should be AT MOST k items in this set
                Set.remove(nums[i-k]) # if more than k items, remove the last-added item
                
        return False
