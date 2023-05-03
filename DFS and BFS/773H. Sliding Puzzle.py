"""
773H. Sliding Puzzle

Description:
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. 
A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. 
If it is impossible for the state of the board to be solved, return -1.

Example 1:
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Example 2:
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Constraints:
board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
"""

"""
Method: The problem is how to formulate the dirs.
        In this case, we track the position of '0'. Use the idx of the neighbors of '0' as movement directions.
        '1 2 3 4 0 5'
         0 1 2 3 4 5
         The idx of neighbors of position 4 are 1, 3, and 5.
         The idx of neighbots of position 1 are 0, 2, and 4.
"""
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = 2, 3
        target = '123450'
        cur_board = []
        for i in range(m):
            for j in range(n):
                cur_board.append(str(board[i][j]))
        start = ''.join(cur_board)

        neighbor = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        q = collections.deque()
        q.append(start)
        visited = set()
        visited.add(start)
        step = 0
        while len(q):
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur == target:
                    return step
                idx = cur.index('0')
                for i in neighbor[idx]:
                    new = self.swap(cur, idx, i)
                    if new not in visited:
                        q.append(new)
                        visited.add(new)
            step += 1
        return -1
    
    def swap(self, cur, idx, i):
        l = list(cur)
        l[idx], l[i] = l[i], l[idx]
        return ''.join(l)


