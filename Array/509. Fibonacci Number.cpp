/*
509. Fibonacci Number
Array

Description:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).


Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
0 <= n <= 30
*/

/* 
Method: If we use the standard recursive approach, the time complexity will be O(2^N).
        Therefore, we need a dictionary to store the values that we have calculated.
*/
class Solution {
public:
    map<int, int> m;
    int fib(int n) {
        if(n<2){
            m[n] = n;
            return n;
        }
        if(m.find(n-1)==m.end()){
            m[n-1] = fib(n-1);
        }
        if(m.find(n-2)==m.end()){
            m[n-2] = fib(n-2);
        }
        return m[n-1] + m[n-2];
    }
};
