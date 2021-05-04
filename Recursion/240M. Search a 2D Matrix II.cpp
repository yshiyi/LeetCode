/*
240M. Search a 2D Matrix II
Binary Search, Divide and Conquer

Description:
Write an efficient algorithm that searches for a target value in an m x n integer matrix. 
The matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109

Similar Question:
Search a 2D Matrix - Medium
*/

// Method 1: time complexity O(n+m)
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
        int i = 0, j = col - 1;
        while(i < row and j >= 0){
            if(matrix[i][j] == target){
                return true;
            }
            if(matrix[i][j] > target){
                j--;
            }else{
                i++;
            }
        }
        return false;
    }
}

// Method 2: Divide and Conquer, much slower than method 1
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int r = 0;
        int c = 0;
        int len = min(rows, cols);
        
        for (int i = 0; i < len; i++) {
            if (matrix[i][i] == target) {
                return true;
            } else if (matrix[i][i] > target) {  // key operation, separating the matrix into four parts.
                r = i;
                c = i;
                break;
            }
        }
        
        for (int i = r; i < rows; i++) {
            for (int j = 0; j <= c; j++) {
                if (matrix[i][j] == target)
                    return true;
            }
        }
        for (int i = 0; i <= r; i++) {
            for (int j = c; j < cols; j++) {
                if (matrix[i][j] == target)
                    return true;
            }
        }
        
        return false;
    }
};
