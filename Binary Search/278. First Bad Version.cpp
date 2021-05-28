/*
278. First Bad Version
Binary Search

Description:
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. 
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

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

/* 
Mehod 1: Using Template I
         There are two different approach: access the right neighbor and access the left neighbor.
         In this solution, we first check mid. If mid is false, we check the right side of the array.
         If mid is true, we check the left neighbor. If the left neightbor is false, then mid is the solution.
         Otherwise, we check the left side of array.
         We need to consider when mid == 1.
*/
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

/*
Method 2: Using Template II
          In this solution, we check the right neighbor. Hence, left < right, as left+1 will exceed the limit.
*/
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while(left < right){
            int mid = left + (right-left)/2;
            // If mid is false and mid+1 is true, then return mid.
            if(!isBadVersion(mid) && isBadVersion(mid+1)){
                return mid+1;
            }
            // If mid is false and mid+1 is false, we check mid+1 ~ right.
            if(!isBadVersion(mid) && !isBadVersion(mid+1)){
                left = mid + 1;
            }
            // As the condition of the while loop is left < right,
            // if right = mid - 1, then we can't examine the value at mid - 1.
            if(isBadVersion(mid)){
                right = mid;
            }
        }
        if(left==right && isBadVersion(left)){return left;}
        return -1;
    }
};
