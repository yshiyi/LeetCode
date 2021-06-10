/*
29M. Divide Two Integers
Math, Binary Seach

Description:
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1

Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
*/

/*
Method: Similar to 69. Sqrt(x)
        The only tricky part is the negative bound of dividend or divisor is -2^31.
        The absolute value of which is out of bound of int.
        Therefore, we should use long instead of int. 
        And the search range is from INT_MIN to INT_MAX.
*/
class Solution {
public:
    int divide(int dividend, int divisor) {
        // This is a special case.
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;
        long left = INT_MIN, right = INT_MAX;
        long num = dividend, den = divisor;
        while (left < right){
            long mid = left + (right-left)/2;
            if(mid == num/den){
                return mid;
            }
            if(mid>num/den){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
