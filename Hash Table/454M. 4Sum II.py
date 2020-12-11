"""
454. 4Sum II
Hash Table, Binary Search

Description:
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0


Similar Questions:
4Sum - Medium
"""

# Solution
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        """
        Method 1: Create a dictionary to store the combinations of A and B.
                  The key the possible summation and the value is the number of appearances.
                  Use dic.get(value, 0). Note, 0 is optional and is the return value when the specific key does not exist.
        """
        n = len(A)
        ans = 0
        Dic_AB = {}
        for i in range(n):
            for j in range(n):
                num = A[i] + B[j]
                Dic_AB[num] = Dic_AB.get(num, 0) + 1
        
        for k in range(n):
            for l in range(n):
                num2 = C[k] + D[l]
                if -num2 in Dic_AB:
                    ans += Dic_AB[-num2]
        
        return ans


"""
Method 2: Similar idea to method 1.
          Use collections.defaultdict to initialize a dictionary.
          Faster than method 1.
"""
from collections import defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d1 =defaultdict(int)
        for i in A:
            for j in B:
                d1[i+j]+=1
        count = 0
        for i in C:
            for j in D:
                count+=d1[-(i+j)] 
        return count
