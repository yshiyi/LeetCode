/*
658M. Find K Closest Elements
Binary Search

Description:
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:
1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

Similar Questions:
Guess Number Higher or Lower - Easy
Guess Number Higher or Lower II - Medium
Find K-th Smallest Pair Distance - Hard
*/

/*
Method 1: Binary Search to find left bound
          Time complexity is O(log(N-k) + k). Take O(log(N-k)) to search for the left bound and O(k) to build the final answer.
          The basic idea is that we use binary search method to determine the position of the left bound.
          First of all, the biggest index the left bound could be is arr.size()-k. Suppose arr.size() = 5, k = 3
          0 1 2 3 4, the biggest index of the left bound is 2.
          Then, we consider arr[mid] and arr[mid+k]. Notice that only one of them could be in a final answer.
          If arr[mid] is closer than arr[mid+k], it means we don't need to consider all the values to the right of arr[mid+k] as well as arr[mid+k]. We should move the right pointer to avoid considering them.
*/
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size()-k;
        while(left < right){
            int mid = left + (right-left)/2;
            if(x-arr[mid]>arr[mid+k]-x){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return vector<int>(arr.begin()+left, arr.begin()+left+k);
    }
};

/*
Method 2: Shrink the size of the array
          Compare arr.front() and arr.back(), and remove the one which is further from x.
          Repeat this process until we reduce the size of the array to k.
*/
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        vector<int> res = arr;
        while(res.size()>k){
            if(x-res.front() <= res.back()-x){
                res.pop_back();
            }else{
                res.erase(res.begin());
            }
        }
        return res;
    }
};
