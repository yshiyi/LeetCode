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
Solution: If we use the brute force approach, the time complexity will be O(n).
          To accelerate the calculation process, we can use divide and conquer approach. The time complexity is O(log(n)).
          1. Divid the whole list into two pieces, and calculate the result for each of them.
          2. If n ia even number, then just return temp * temp. If n is an odd number, then return temp * temp * x.
*/
class Solution {
public:
    double myPow(double x, int n) {
        // Brute force recursion
        // double res = 1.0;
        // if(n==0){
        //     return 1.0;
        // }
        // res = x * myPow(x, abs(n)-1);
        // if(n>0){
        //     return res;
        // }else{
        //     return 1/res;
        // }
        
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
