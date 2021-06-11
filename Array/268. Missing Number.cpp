/*
268. Missing Number
Array, Math, Bit Manipulation

Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
             2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
             2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
             8 is the missing number in the range since it does not appear in nums.

Example 4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 
             1 is the missing number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

Similar Questions:
First Missing Positive - Hard
Single Number - Easy
Find the Duplicate Number - Medium
Couples Holding Hands - Hard
*/

/*
Method: According to the description of the problem, we notice that the values contained in the array are unique and consecutive except the missing one.
        If we calculate the summation from 0 to n, and subtract the summation of all values in the array, the result is the missing value.
        e.g. [3, 0, 1]
        sum(0,1,2,3) = 6, sum([3,0,1]) = 4
*/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int l = nums.size();
        int sum = l*(l+1)/2;
        for(auto v:nums){
            sum -= v;
        }
        return sum;
    }
};
