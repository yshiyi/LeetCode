"""
990M. Satisfiability of Equality Equations.py

Description:
You are given an array of strings equations that represent relationships between variables 
where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.


Example 1:
Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:
Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
 

Constraints:
1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""

"""
Method: This is a typical problem that can be solved by using union-find approach.
        For the letters that are connected by "==", we group them.
        At the end, we check those equations contains "!=". If the letters are connected, then return false.
"""
class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        class UF:
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.size = [1] * n
            
            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p
            
            def union(self, p, q):
                rootP, rootQ = self.find(p), self.find(q)
                if rootP == rootQ:
                    return
                if self.size[rootP] > self.size[rootQ]:
                    self.parent[rootQ] = rootP
                    self.size[rootP] += self.size[rootQ]
                else:
                    self.parent[rootP] = rootQ
                    self.size[rootQ] += self.size[rootP]
                return
            
            def connect(self, p, q):
                return self.find(p) == self.find(q)
        
        uf = UF(26)
        for equ in equations:
            if equ[1] == '=':
                uf.union(ord(equ[0])-ord('a'), ord(equ[3])-ord('a'))
        for equ in equations:
            if equ[1] == '!':
                if uf.connect(ord(equ[0])-ord('a'), ord(equ[3])-ord('a')):
                    return False
        
        return True
