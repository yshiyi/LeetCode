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
2 <= n <= 10^4
0 <= nums[i] <= 10^6
1 <= k <= n * (n - 1) / 2

Similar Questions:
Find K Pairs with Smallest Sums - Medium
Kth Smallest Element in a Sorted Matrix - Medium
Find K Closest Elements - Medium
Kth Smallest Number in Multiplication Table - Hard
K-th Smallest Prime Fraction - Hard
*/

/*
Method 1: Based on the constraints of the question, we can see that the maximum distance is 10^6 (10^6 - 0).
          In other words, there are 10^6 possible distances.
          Then, we create a vector with size of 10^6, and each position in the vector is corresponding to that value of distance.
          e.g. dis[1] = 2 represents there are two distances with value 1.
          We then traverse the entire nums and calculate all possible distance.
          Save the distance value to the corresponding position in the vector dis.
          Finally, we calculate the sum of dis from dis[0] until the sum is greater or equal to k.
          Then that index in dis is the answer.
          This method works, but really slow.
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


/*
Method 2: Binary Search.
          We don't search a particular value in nums. Instead, we search for the particular value of distance that satisfies the question requirement.
          We sort the vector first.
          The minimum distance is 0, and the maximum distance is the distance between the last and the first element.
          Then we will search for the answer within this range.
          mid = left+(right-left)/2 as usual. Then for this value of distance, we need to traverse nums and find out the number of distance that is less than or equal to mid.
          If the number is greater or equal to k, it means the value of mid is large, and we need to move right pointer.
          Otherwise, we move left pointer.
*/
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.back()-nums[0];
        while(left<right){
            int mid = left + (right-left)/2;
            int count = 0, j = 0;
            
            /*
            This is the brute force method. It will exceed the time limitation.
            for(int i=0; i<nums.size()-1; ++i){
                for(int j=i+1; j<nums.size(); ++j){
                    if(nums[j] - nums[i] <=mid){
                        ++count;
                    }
                }
            }
            */
            
            /*
            In this method, we use two pointers technique.
            The second pointer keeps moving, if nums[j] - nums[i] <= mid.
            The tricky part is that for the next iteration of i, we don't need to reset j back to i+1.
            Because we have sorted the array, if nums[5] - nums[0] < mid, then nums[5] - nums[1] must be less than mid too.
            */
            for(int i=0; i<nums.size()-1; ++i){
                while(j<nums.size() && nums[j]-nums[i]<=mid){
                    ++j;
                }
                count += j - i - 1;
            }
            
            /*
            This method is little faster than the previous one.
            In this method, we use i to traverse nums.
            We keep moving i until nums[i] - nums[start] > mid.
            Then we count the difference between i and start, and move start forward by 1.
            */
            // int mid = left + (right - left) / 2, count = 0, start = 0;
            // for (int i = 0; i < nums.size(); ++i) {
            //     while (start < nums.size() && nums[i] - nums[start] > mid) ++start;
            //     count += i - start;
            // }
            
            if(count>=k){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};

