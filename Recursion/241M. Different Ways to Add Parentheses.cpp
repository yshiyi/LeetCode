/*
241. Different Ways to Add Parentheses
Divide and Conquer

Description:
Given a string expression of numbers and operators, 
return all possible results from computing all the different possible ways to group numbers and operators. 
You may return the answer in any order.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.

Similar Questions:
Unique Binary Search Trees II - Medium
Basic Calculator - Hard
Expression Add Operators - Hard
*/

/*
Method : Divide and Conquer
         Given an example: 2-1-1. The two possible solutions are:
         (2-1) - (1) = 0
         (2) - (1-1) = 2
         We can see we seperate the equation at the any operator.
         The final solution is the combination of the result from the left and that from the right
*/
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int> res;
        for(int i=0; i<expression.size(); i++){
            char c = expression[i];
          
            // If there is an operator, we seperate the expression into left part and right part.
            if(c=='+'||c=='-'||c=='*'){
                // Both left and right part contains all possible results.
                vector<int> left = diffWaysToCompute(expression.substr(0, i));
                vector<int> right = diffWaysToCompute(expression.substr(i+1));
                
                // We then combine the results from left and right based on the operator.
                for(auto vl:left){
                    for(auto vr:right){
                        if(c=='+'){
                            res.push_back(vl+vr);
                        }else if(c=='-'){
                            res.push_back(vl-vr);
                        }else if(c=='*'){
                            res.push_back(vl*vr);
                        }
                    }
                }
            }
        }
        
        /* This part defines the base case.
           If there is nothing added to the res, it means there is no operator.
           It means the expression only contains a sinlge number.
        */
        if(res.empty()){
            res.push_back(stoi(expression));
        }
        return res;
    }
};
