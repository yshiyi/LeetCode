/*
162M. Find Peak Element
Array, Binary Search

Description:
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

Similar Question:
Peak Index in a Mountain Array - Easy
*/


/*
Method 1: Using Template II
          At the beginning of each iteration, we need to check if mid is 0.
          If mid is not 0, we need to check four possible scenarios.
*/
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if(nums.size()==1){
            return 0;
        }
        int left = 0, right = nums.size()-1;
        while(left < right){
            int mid = left + (right-left)/2;
            cout << mid << endl;
            if(mid==0 && nums[mid]>nums[mid+1]){
                return mid;
            }else if(mid==0 && nums[mid]<nums[mid+1]){
                left = mid + 1;
            }
            if(mid!=0){
                if(nums[mid]>nums[mid-1] && nums[mid]>nums[mid+1]){
                    return mid;
                }else if(nums[mid-1]>nums[mid] && nums[mid]>nums[mid+1]){
                    right = mid;
                }else if(nums[mid-1]<nums[mid] && nums[mid]<nums[mid+1]){
                    left = mid + 1;
                }else if(nums[mid-1]>nums[mid] && nums[mid]<nums[mid+1]){
                    left = mid + 1;
                }
            }
        }
        // The final scenario is when we reach to the end of array.
        if(left==right && nums[left]>nums[left-1]){
            return left;
        }
        return -1;
    }
};

/*
Method 2: This is straightforward. But a little slower than method 1.
*/
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        while(left < right){
            int mid = left + (right-left)/2;
            if(nums[mid]>nums[mid+1]){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
