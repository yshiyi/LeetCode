/*
167. Two Sum II - Input array is sorted
Array, Two Pointers, Binary Search

Description:
Given an array of integers numbers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, 
where 1 <= answer[0] < answer[1] <= numbers.length.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]

Similar Questions:
Two Sum - Easy
Two Sum IV - Input is a BST - Easy
Two Sum Less Than K - Easy
*/


/* Method: Two Pointers.
           One pointer starts from left, and one starts from right.
           If summation is greater than the target, move the right pointer left.
           If summation is less than the target, move the left pointer right.
*/
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size()-1;
        vector<int> res;
        while(left<right){
            int sum = numbers[left] + numbers[right];
            if(sum==target){
                res.push_back(left+1);
                res.push_back(right+1);
                break;
            }else if(sum>target){
                right--;
            }else if(sum<target){
                left++;
            }
        }
        return res;
    }
};
