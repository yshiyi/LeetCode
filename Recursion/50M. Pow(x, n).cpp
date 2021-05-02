/*
50M. Pow(x, n)
Math, Binary Search

Dexcription:
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

Similar Question:
Sqrt(x) - Easy
Super Pow - Medium
*/

/*
Solution: 
*/
class Solution {
public:
    double myPow(double x, int n) {
        if(n>=0){
            return helper(x, n);
        }else {
            return 1/helper(x, abs(n));
        }
    }
    double helper(double x, int n){
        if(n==0){
            return 1.0;
        }else if(n == 1){
            return x;
        }
        double temp = helper(x, n/2);
        if (n % 2 == 0) {
            return temp * temp;
        }else{
            return temp * temp * x;
        }
    }
};
