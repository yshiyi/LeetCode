/*
67. Add Binary
Math, String

Description:
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Similar Questions:
Add Two Numbers - Medium
Multiply Strings - Medium
Plus One - Easy
Add to Array-Form of Integer - Easy
*/

class Solution {
public:
    string addBinary(string a, string b) {
        stack<int> sa, sb;
        for(auto& c:a){
            sa.push((int)c-48);
        }
        for(auto& c:b){
            sb.push((int)c-48);
        }
        int carry = 0, sum;
        stack<int> s_sum;
        while(sa.size()>0 && sb.size()>0){
            sum = sa.top() + sb.top() + carry;
            if(sum < 2){
                s_sum.push(sum);
                carry = 0;
            }else if(sum==2){
                s_sum.push(0);
                carry = 1;
            }else{
                s_sum.push(1);
                carry = 1;
            }
            sa.pop(); sb.pop();
        }
        while(sa.size()>0){
            sum = sa.top() + carry;
            if(sum < 2){
                s_sum.push(sum);
                carry = 0;
            }else if(sum==2){
                s_sum.push(0);
                carry = 1;
            }else{
                s_sum.push(1);
                carry = 1;
            }
            sa.pop();
        }
        while(sb.size()>0){
            sum = sb.top() + carry;
            if(sum < 2){
                s_sum.push(sum);
                carry = 0;
            }else if(sum==2){
                s_sum.push(0);
                carry = 1;
            }else{
                s_sum.push(1);
                carry = 1;
            }
            sb.pop();
        }
        if(carry==1){
            s_sum.push(carry);
        }
        string res="";
        while(s_sum.size()>0){
            res += (char)(s_sum.top() + 48);
            s_sum.pop();
        }
        return res;
    }
};
