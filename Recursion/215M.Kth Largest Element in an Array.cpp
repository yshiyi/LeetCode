/*
215M. Kth Largest Element in an Array
Divide and Conquer, Heap

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
Wiggle Sort II Medium
Top K Frequent Elements - Medium
Third Maximum Number - Easy
Kth Largest Element in a Stream - Easy
K Closest Points to Origin - Medium
*/

/*
Method 1: Quickselect approach
          Instead of sweeping the vector from left, we sweep the vector from right.
          At the end of partition function, we should swap nums[++i] and nums[pivot_index] to ensure all the values
          on the right side of pivot are greater than it.
          In this script, we select the most rightmost value as the pivot.
          The run time is about 40 ms.
*/
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return quickSelect(nums, 0, nums.size()-1, k);
    }
    int quickSelect(vector<int>& nums, int left, int right, int k){
        // if(k<=right-left+1){
        if(right>=left){ 
            int pivot_index = partition(nums, left, right);
            if(right - pivot_index == k-1){
                return nums[pivot_index];
            }
            if(right - pivot_index > k-1){
                return quickSelect(nums, pivot_index+1, right, k);
            }else{
                return quickSelect(nums, left, pivot_index-1, k-(right-pivot_index+1));
            }
        }
        return -1;
    }
    int partition(vector<int>& nums, int left, int right){
        int pivot = nums[right];
        int pivot_index = right-1;
        for(int i=right-1; i>=left; i--){
            if(nums[i] >= pivot){
                swap(nums[i], nums[pivot_index]);
                pivot_index--;
            }
        }
        swap(nums[++pivot_index], nums[right]);
        return pivot_index;
    }
};

/*
Method 2: In this script, we randomly select the pivot.
          Note, we need to record the new position of the pivot.
          The run time is about 4-8 ms.
*/
int partition(vector<int>& nums, int left, int right){
    if(right==left){
        return left;
    }
    int pivot_index = rand() % (right-left+1) + left;
    int pivot = nums[pivot_index];
    int i = right;
    for(int j=right;j>=left;j--){
        if(nums[j]>=pivot){
            swap(nums[j], nums[i]);
            if(j==pivot_index){
                pivot_index = i;
            }
            i--;
        }
    }
    swap(nums[++i], nums[pivot_index]);
    return i;
}
