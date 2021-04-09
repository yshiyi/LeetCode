/*
119. Pascal's Triangle II
Array

Description:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
1
11
121
1331
14641

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Similar Question:
Pascal's Triangle - Easy
*/


class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result;
        result.resize(rowIndex + 1);
        result[0] = 1;
        result[rowIndex] = 1;
        for (int i = 1; i <= rowIndex; ++i) {
            result[i] = 1;
            for (int j = i - 1; j > 0; --j) {
                result[j] = result[j] + result[j - 1];
            }
        }
        return result;
      }
};
