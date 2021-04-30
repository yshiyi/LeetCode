/*
70. Climbing Stairs
Dynamic Programming

Description:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45

Similar Question:
Min Cost Climbing Stairs - Easy
Fibonacci Number - Easy
N-th Tribonacci Number - Easy
*/

// Solution:
class Solution {
public:
    map<int, int> m;
    int climbStairs(int n) {
        if(n<3){
            m[n] = n;
            return n;
        }
        if(m.find(n-1)==m.end()){
            m[n-1] = climbStairs(n-1);
        }
        if(m.find(n-2)==m.end()){
            m[n-2] = climbStairs(n-2);
        }
        return m[n-1] + m[n-2];
    }
};
