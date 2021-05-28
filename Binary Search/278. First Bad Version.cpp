/*
278. First Bad Version
Binary Search

Description:
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 231 - 1

Similar Questions:
Find First and Last Position of Element in Sorted Array - Medium
Search Insert Position - Easy
Guess Number Higher or Lower - Easy
*/

// Mehod 1: Using Template I
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while(left <= right){
            int mid = left + (right-left)/2;
            if(!isBadVersion(mid)){
                left = mid + 1;
            }else{
                if(mid==1){
                    return mid;
                }
                if(!isBadVersion(mid-1)){
                    return mid;
                }else{
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
};
