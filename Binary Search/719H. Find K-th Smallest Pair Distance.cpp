/*
719H. Find K-th Smallest Pair Distance
Array, Binary Search, Heap

Description:
The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,1,1], k = 2
Output: 0

Example 3:
Input: nums = [1,6,1], k = 3
Output: 5

Constraints:
n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2

Similar Questions:
Find K Pairs with Smallest Sums - Medium
Kth Smallest Element in a Sorted Matrix - Medium
Find K Closest Elements - Medium
Kth Smallest Number in Multiplication Table - Hard
K-th Smallest Prime Fraction - Hard
*/

/*
Method 1:
*/
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        vector<int> dis(1000000, 0);
        for(int i=0; i<nums.size()-1;++i){
            for(int j=i+1; j<nums.size(); ++j){
                ++dis[abs(nums[i]-nums[j])];
            }
        }
        int count = 0;
        int res = 0;
        for(int i=0; i<dis.size(); ++i){
            count += dis[i];
            if(count>=k){
                res = i;
                break;
            }
        }
        return res;
    }
};
