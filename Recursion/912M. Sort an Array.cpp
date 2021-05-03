/*
912M. Sort an Array

Description:
Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
*/

// Method 1: Merge sort
class Solution {
public:
    int pivot;
    vector<int> sortArray(vector<int>& nums) {
        if(nums.size()<2){
            return nums;
        }
        vector<int> left, right;
        pivot = nums.size()/2;
        for(int i=0; i<pivot; i++){
            left.push_back(nums[i]);
        }
        for(int i=pivot; i<nums.size();i++){
            right.push_back(nums[i]);
        }
        return merge(sortArray(left), sortArray(right));
    }
    vector<int> merge(vector<int> left, vector<int> right){
        int l = 0, r = 0;
        vector<int> res;
        while(l<left.size() && r<right.size()){
            if(left[l]<=right[r]){
                res.push_back(left[l]);
                l++;
            }else{
                res.push_back(right[r]);
                r++;
            }
        }
        if(l==left.size()){
            for(int i=r;r<right.size(); r++){
                res.push_back(right[r]);
            }
        }
        if(r==right.size()){
            for(int i=l; l<left.size(); l++){
                res.push_back(left[l]);
            }
        }
        return res;
    }
};

