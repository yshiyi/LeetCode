/*
378M. Kth Smallest Element in a Sorted Matrix
Binary Search, Heap

Description:
Given an n x n matrix where each of the rows and columns are sorted in ascending order, 
return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

Similar Questions:
Find K Pairs with Smallest Sums - Medium
Kth Smallest Number in Multiplication Table - Hard
Find K-th Smallest Pair Distance - Hard
K-th Smallest Prime Fraction - Hard
*/

/*
Method: Binary Seach
        At first, we need to determine the range of search. 
        In this problem, left is the smallest value in the matrix which is the first one in the first row.
        Right is the largest value which is the last one in the last row.
        We use binary search to find the first value that is greater than or equal to k.
        The tricky part is to determine the number of values that are not greater than mid.
        We can first compare the last value in each row. If mid is greater than that, then count += n.
        Otherwise, we need to compare the first value in each row. If mid is greater, then we enter that row.
*/
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int left = matrix[0].front(), right = matrix.back().back();
        return binarySearch(matrix, left, right, k);
    }
    int binarySearch(vector<vector<int>>& matrix, int left, int right, int k){
        int n = matrix.size();
        while(left < right){
            int mid = left + (right-left)/2;
            int count = 0;
            // Calculate # of values less 
            for(int i=0; i<n; ++i){
                if(matrix[i].back()<=mid){
                    count += n;
                }else{
                    if(matrix[i].front()>mid){
                        break;
                    }else{
                        for(int j=0; j<n; ++j){
                            if(matrix[i][j]<=mid){
                                ++count;
                            }else{
                                break;
                            }
                        }
                    }
                }
            }
            
          if(count>=k){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
