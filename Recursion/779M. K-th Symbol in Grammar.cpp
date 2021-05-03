/*
779M. K-th Symbol in Grammar
Recursion

Description:
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
*/

/* 
Solution: Consider the base case first, where we should return 0 when N==1.
          Then the recurrence relation, if K is an even number then, we should inquire the K/2 th number in the previous row.
          If K is an odd number, then we should inquire the K/2+1 th number in the previous row.
*/
class Solution {
public:
    int pre;
    int kthGrammar(int N, int K) {
        if(N==1){
            return 0;
        }
        if(K%2==0){
            pre = kthGrammar(N-1, K/2);
        }else{
            pre = kthGrammar(N-1, K/2+1);
        }
        if(pre==0 && K%2==0){
            return 1;
        }else if(pre==0 && K%2==1){
            return 0;
        }else if(pre==1 && K%2==0){
            return 0;
        }else{
            return 1;
        }
    }
};
