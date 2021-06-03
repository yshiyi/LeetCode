/*
367. Valid Perfect Square
Math, Binary Search

Description:
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:
1 <= num <= 2^31 - 1

Similar Questions:
Sqrt(x) - Easy
Sum of Square Numbers - Medium
*/

/*
Method: Binary Search
        Both right=num and right=num/2 work.
        We compare mid^2 with num. If mid^2>num, we move left. Otherwise, we move right.
*/
class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==1){
            return true;
        }
        int left = 1, right = num/2;
        while(left <= right){
            int mid = left + (right-left)/2;
            // Note: num/mid return an int, e.g., 5/2 -> 2. We need to convert the result to double.
            if((double)num/mid==mid){
                return true;
            }
            if(mid>num/mid){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return false;
    }
};
