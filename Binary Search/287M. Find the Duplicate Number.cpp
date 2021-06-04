/*
287M. Find the Duplicate Number
Array, Two pointers, Binay Search

Description:
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

Similar Questions:
First Missing Positive - Hard
Single Number - Easy
Linked List Cycle II - Medium
Missing Number - Easy
Set Mismatch - Easy
*/

/*
Method: If we want to distribute n+1 objects to n boxes, there must be one box that contains more than one object.
        Using this idea, let mid = (left + right)/2, and compare each value in nums with mid.
        If the number of values that are less than or equal to mid is greater than mid, then the duplicate value must be less than or equal to mid.
*/
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int left = 1, right = nums.size();
        while (left < right){
            int mid = left + (right - left) / 2, cnt = 0;
            for (int num : nums) {
                if (num <= mid) ++cnt;
            }
            if (cnt <= mid) left = mid + 1;
            else right = mid;
        }    
        return right;
    }
};
