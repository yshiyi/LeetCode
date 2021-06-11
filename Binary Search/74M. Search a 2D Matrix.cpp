/*
74M. Search a 2D Matrix
Array, Binary Search

Description:
Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

Similar Question:
Search a 2D Matrix II - Medium
*/

/*
Method: Binary Search
        If a question ask us to search for a particular value, then the first choice of method is Binary Search.
        From the description of the question, we can see that the first value in each row is greater than the last one in the previous row.
        Hence, we can apply binary search on the first column and find the first the value that is greater than target.
        Then target must be in the previoud row.
*/
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(target<matrix[0][0]){
            return false;
        }
        // Apply Binary Search on the first column and determine the row that target lies in
        int left = 0, right = matrix.size();
        while(left<right){
            int mid = left + (right-left)/2;
            if(matrix[mid].front()==target){
                return true;
            }
            if(matrix[mid].front()<target){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        int row = left - 1;

        // Search for target in the particular row
        int lr = 0, rr = matrix[row].size();
        while(lr < rr){
            int mid = lr + (rr-lr)/2;
            if(matrix[row][mid]==target){
                return true;
            }
            if(matrix[row][mid]<target){
                lr = mid + 1;
            }else{
                rr = mid;
            }
        }
        
        return false;
    }
};
