/*
69. Sqrt(x)
Math, Binary Search

Description:
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:
0 <= x <= 231 - 1
*/

// Method 1:
class Solution {
public:
    int mySqrt(int x) {
        if(x<2){
            return x;
        }
        int left = 0, right = x;
        while(left<=right){
            int mid = (right+left)/2;
            if(mid<=x/mid && (mid+1)>x/(mid+1)){
                return mid;
            }
            if(mid>x/mid){
                right = mid-1;
            }
            if(mid<x/mid){
                left = mid + 1;
            }
        }
        return -1;
    }
};

// Method 2:
class Solution {
public:
    int mySqrt(int x) {
        if(x<2){
            return x;
        }
        int left = 0, right = x;
        while(left<right){
            int mid = (right+left)/2;
            if(mid<=x/mid){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left-1;
    }
};
