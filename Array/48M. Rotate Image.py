'''
48. Rotate Image
Array

Description:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]
'''

# Solution:
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        '''
        Method 1: Rotate Four rectangles
                  For a 3*3 matrix, observe that (0,0) -> (2,0) -> (2,2) -> (0,2).
                  We only need to do this rotation for half of the matrix (i.e., len(matrix)//2). 
                  If the size of the matrix is an odd number, we only need to do the rotation for less than half of the matrix.
                  As moving down the matrix, we can gradually consider two less element (i.e., one at the beginning and one at the end).
                  Switch the elements at each step. Repeat this switch for three times for each round.
                  Time complexity: O(N^2); Space complexity: O(1)
        '''
        # i: row number
        for i in range(len(matrix) // 2):
            # j : column number
            for j in range(0 + i, len(matrix) - i - 1, 1):
                # index1 = i
                # index2 = j
                # temp1 = matrix[i][j]
                # for k in range(4):
                #     temp2 = matrix[index2][len(matrix)-index1-1]
                #     matrix[index2][len(matrix)-index1-1] = temp1
                #     temp1 = temp2
                #     index_temp = index1
                #     index1 = index2
                #     index2 = len(matrix)-index_temp-1
                row, col = i, j
                for k in range(3):
                    matrix[len(matrix)-col-1][row], matrix[row][col] = matrix[row][col], matrix[len(matrix)-col-1][row]
                    row, col = len(matrix)-col-1, row
        return matrix
        
        
        '''
        Method 2: Transpose and then reverse
                  Observe that we can obtain the result by transposing the matrix first and then reversing each row.
                  Time complexity: O(N^2); Space complexity: O(1)
        '''
        n = len(matrix[0])        
        # transpose matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        
        # reverse each row
        for i in range(n):
            matrix[i].reverse()
        
        
        '''
        Method 3: Rotate Four rectangles in one single loop
                  Following the idea of Method 1, we do the rotation in one single loop.
                  Time complexity: O(N^2); Space complexity: O(1)
        '''
        l = len(matrix)
        for i in range(l // 2):
            for j in range(0 + i, l - i - 1, 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[l-j-1][i]
                matrix[l-j-1][i] = matrix[l-i-1][l-j-1]
                matrix[l-i-1][l-j-1] = matrix[j][l-i-1]
                matrix[j][l-i-1] = tmp

