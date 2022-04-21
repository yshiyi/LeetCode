<!-- GFM-TOC -->
* [Heap](#Heap)
    * [215. Kth Largest Element in an Array](#215-Kth-Largest-Element-in-an-Array)
    * [347. Top K Frequent Elements](#347-Top-K-Frequent-Elements)
    * [23. Merge K Sorted Lists](#23-Merge-K-Sorted-Lists)
    * [378. Kth Smallest Element in a Sorted Matrix](#378-Kth-Smallest-Element-in-a-Sorted-Matrix)
    * [973. K Closest Points to Origin](#973-K-Closest-Points-to-Origin)
* [BFS](#BFS)
    * [1091. Shortest Path in Binary Matrix](#1091-Shortest-Path-in-Binary-Matrix)
    * [199. Binary Tree Right Side View](#199-Binary-Tree-Right-Side-View)
    * [103. Binary Tree Zigzag Level Order Traversal](#103-Binary-Tree-Zigzag-Level-Order-Traversal)
    * [515. Find Largest Value in Each Tree Row](#515-Find-Largest-Value-in-Each-Tree-Row)
    * [314. Binary Tree Vertical Order Traversal](#314-Binary-Tree-Vertical-Order-Traversal)
    * [987. Vertical Order Traversal of a Binary Tree](#987-Vertical-Order-Traversal-of-a-Binary-Tree)
    * [133. Clone Graph](#133-Clone-Graph)
    * [1036. Escape a Large Maze](#1036-Escape-a-Large-Maze)

* [DFS Backtracking](#DFS-Backtracking)
    * [113. Path Sum III](#113-Path-Sum-III)
    * [863. All Nodes Distance K in Binary Tree](#863-All-Nodes-Distance-K-in-Binary-Tree)
    * [333. Largest BST Subtree](#333-Largest-BST-Subtree)
    * [543. Diameter of Binary Tree](#543-Diameter-of-Binary-Tree)
    * [78. Subsets](#78-Subsets)
    * [90. Subsets II](#90-Subsets-II)
* [Stack](#Stack)
    * [227. Basic Calculator II](#227-Basic-Calculator-II)
    * [1762. Building With an Ocean View](#1762-Building-With-an-Ocean-View)
    * [1249. Minimum Remove to Make Valid Parentheses](#1249-Minimum-Remove-to-Make-Valid-Parentheses)
    * [921. Minimum Add to Make Parentheses Valid](#921-Minimum-Add-to-Make-Parentheses-Valid)
* [Recursion](#Recursion)
    * [339. Nested List Weight Sum](#339-Nested-List-Weight-Sum)
    * [50. Pow(x, n)](#50-Pow-x-n)
    * [426. Converted Binary Search Tree to Sorted Doubly Linked List](#426-Converted-Binary-Search-Tree-to-Sorted-Doubly-Linked-List)
    * [124. Binary Tree Maximum Path Sum](#124-Binary-Tree-Maximum-Path-Sum)
* [Binary Tree](#Binary-Tree)
    * [236. Lowest Common Ancestor of a Binary Tree](#236-Lowest-Common-Ancestor-of-a-Binary-Tree)
    * [1650. Lowest Common Ancestor of a Binary Tree III](#1650-Lowest-Common-Ancestor-of-a-Binary-Tree-III)
    * [173. Binary Search Tree Iterator](#173-Binary-Search-Tree-Iterator)
    * [Sorted Iterator](#Sorted-Iterator)

* [Array](#Array)
    * [56. Merge Intervals](#56-Merge-Intervals) 
    * [Max Product of K elements in an array](#Max-Product-of-K-elements-in-an-array)
    * [560. Subarray Sum Equals K](#560-Subarray-Sum-Equals-K)
* [Two Pointers](#Two-Pointers)
    * [408. Valid Word Abbreviation](#408-Valid-Word-Abbreviation)
    * [680. Valid Palindrome-II](#680-Valid-Palindrome-II)
    * [125. Valid Palindrome](#125-Valid-Palindrome)
    * [346. Moving Average from Data Stream](#346-Moving-Average-from-Data-Stream)
    * [88. Merge Sorted Array](#88-Merge-Sorted-Array)
    * [139. Word Break](#139-Word-Break)
* [Hash Table](#Hash-Table)
    * [939. Minimum Area Rectangle](#939-Minimum-Area-Rectangle)
    * [791. Custom Sort String](#791-Custom-Sort-String)
    * [13. Roman to Integer](#13-Roman-to-Integer)
    * [Flip a number over 180 degrees](#Flip-a-number-over-180-degrees)
* [Binary Search](#Binary-Search)
    * [528. Random Pick with Weight](#528-Random-Pick-with-Weight)
    * [Cut Wood](#Cut-Wood)
    * [658. Find K Closeest Elements](#658-Find-K-Closeest-Elements)
* [String](#String)
    * [65. Valid Number](#65-Valid-Number)
    * [415. Add Strings](#415-Add-Strings)
    * [71. Simplify Path](#71-Simplify-Path)

* [Others](#Others)
    * [1570. Dot Product of Two Sparse Vectors](#1570-Dot-Product-of-Two-Sparse-Vectors)
    * [311. Sparse Matrix Multiplication](#311-Sparse-Matrix-Multiplication)
    * [Medium Filter](#Medium-Filter)
    * [Candy Crash 1D](Candy-Crash-1D)
    * [Logical values](Logical-values)
<!-- GFM-TOC -->

# Heap
## 215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.\
Note that it is the kth largest element in the sorted order, not the kth distinct element.\
Example 1:\
Input: nums = \[3,2,1,5,6,4\], k = 2\
Output: 5\
**Constraints:**\
1 <= k <= nums.length <= 104\
-104 <= nums\[i\] <= 104\
**Method:**\
Create a heap to store k element. Pop the top one when length of the heap is greater than k.\
Time complexity: O(Nlogk), using O(logk) to maintain the heap\
Space complexity: O(k)
```
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        heapq.heapify(h)
        for num in nums:
            heapq.heappush(h, num)
            if len(h)>k:
                heapq.heappop(h)
        return h[0]
```

## 347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. \
You may return the answer in any order.\
Example 1:\
Input: nums = \[1,1,1,2,2,3\], k = 2\
Output: \[1,2\]\
**Constraints:**\
1 <= nums.length <= 105\
k is in the range \[1, the number of unique elements in the array\].\
It is guaranteed that the answer is unique.\
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.\
**Method:**\
Use a Counter to count the frequency of each element. Then create a heap to store k elements.\
Each element in the heap is a tuple. The first entry is the frequency, and the second entry is the number.\
Time complexity: O(N+Mlogk), N is the total number of elements in nums, M is the number of elements in the dic.\
Space complexity: O(M), M is always greater than or equal to k.\
```
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        h = []
        heapq.heapify(h)
        for num in count.keys():
            heapq.heappush(h, (count[num], num))
            if len(h)>k:
                heapq.heappop(h)
        ans = []
        for frq, val in h:
            ans.append(val)
        return ans
```

## 23. Merge K Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.\
Merge all the linked-lists into one sorted linked-list and return it.\
Example 1:\
Input: lists = \[\[1,4,5\],\[1,3,4\],\[2,6\]\]\
Output: \[1,1,2,3,4,4,5,6\]\
Explanation: The linked-lists are:\
\[1->4->5, 1->3->4, 2->6\]\
merging them into one sorted list:\
1->1->2->3->4->4->5->6\
Example 2:\
Input: lists = \[\]\
Output: \[\]\
Example 3:\
Input: lists = \[\[\]\]\
Output: \[\]\
**Constraints:**\
k == lists.length\
0 <= k <= 104\
0 <= lists\[i\].length <= 500\
-104 <= lists\[i\]\[j\] <= 104\
lists\[i\] is sorted in ascending order.\
The sum of lists\[i\].length will not exceed 104.\
**Method:**\
Create a heap, and put all the first node and its value into the heap.\
While the heap is not empty, we pop the first element, create a new node, and move to the next.\
Time complexity: O(Nlogk), N is the total nodes in the whole list.\
Space complexity: O(N), create a new linked list.
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        heapq.heapify(h)
        for list in lists:
            if list is not None:
                heapq.heappush(h, (list.val, list))
        head = ListNode()
        cur = head
        while len(h):
            val, node = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            if node.next is not None:
                node = node.next
                heapq.heappush(h, (node.val, node))
        return head.next
```

## 378. Kth Smallest Element in a Sorted Matrix
Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
return the kth smallest element in the matrix.\
Note that it is the kth smallest element in the sorted order, not the kth distinct element.\
You must find a solution with a memory complexity better than O(n2).\ 
Example 1:\
Input: matrix = \[\[1,5,9\],\[10,11,13\],\[12,13,15\]\], k = 8\
Output: 13\
Explanation: The elements in the matrix are \[1,5,9,10,11,12,13,13,15\], and the 8th smallest number is 13\
Constraints:\
n == matrix.length == matrix\[i\].length\
1 <= n <= 300\
-109 <= matrix\[i\]\[j\] <= 109\
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.\
1 <= k <= n2\
**Follow up:**\
Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?\
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.\
Time complexity: O(klogk), we only need to run k times.\
Space complexity: O(k), space for the heap
```
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        r, c = len(matrix), len(matrix[0])
        h = []
        heapq.heapify(h)
        for i in range(min(r, k)):
            heapq.heappush(h, (matrix[i][0], i, 0))
        
        ans = -1
        for i in range(k):
            ans, row, col = heapq.heappop(h)
            if col+1<c:
                heapq.heappush(h, (matrix[row][col+1], row, col+1))
        return ans
```

## 973. K Closest Points to Origin
Given an array of points where points\[i\] = \[xi, yi\] represents a point on the X-Y plane and an integer k, \
return the k closest points to the origin (0, 0).\
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).\
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).\
Example 1:\
Input: points = \[\[1,3\],\[-2,2\]\], k = 1\ 
Output: \[\[-2,2\]\]\
Explanation:\
The distance between (1, 3) and the origin is sqrt(10).\
The distance between (-2, 2) and the origin is sqrt(8).\
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.\
We only want the closest k = 1 points from the origin, so the answer is just \[\[-2,2\]\].\
Constraints:\
1 <= k <= points.length <= 104\
-104 < xi, yi < 104\
**Method:**\
Use max heap. Specifically, we save the negative distance into the heap.\
Time complexity: O(Nlogk)
Space complexity: O(k)
```
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        h = []
        heapq.heapify(h)
        for point in points:
            dis = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(h, (-dis, point))
            if len(h)>k:
                heapq.heappop(h)
        ans = []
        while len(h):
            d, point = heapq.heappop(h)
            ans.append(point)
        return ans
```

#  BFS
## 1091. Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.\
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:\
All the visited cells of the path are 0.\
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).\
The length of a clear path is the number of visited cells of this path.\
**Method:**\
Use BFS.
Time complexity: O(N^2)\
Space complexity: O(N^2)
```
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0]==1:
            return -1
        n = len(grid)
        step = 1
        q = collections.deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        dirs = [[0, 1], [1, 1], [1, 0], [1, -1],
                [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        while len(q):
            size = len(q)
            for _ in range(size):
                curx, cury = q.popleft()
                if curx==n-1 and cury==n-1:
                    return step
                for d in dirs:
                    newx = curx + d[0]
                    newy = cury + d[1]
                    if newx<0 or newx>=n or newy<0 or newy>=n or (newx, newy) in visited or grid[newx][newy]==1:
                        continue
                    visited.add((newx, newy))
                    q.append((newx, newy))
            step += 1
        return -1
```

## 199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.\
Constraints:\
The number of nodes in the tree is in the range \[0, 100\].\
-100 <= Node.val <= 100\
**Method: **\
Use BFS. save the node from right to left, and save the first element.\
Time complexity: O(N)\
Space complexity: O(N)
```
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        ans = []
        while len(q):
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i==0:
                    ans.append(node.val)
                if node.right:
                    q.append(node.right)
                elif node.left:
                    q.append(node.left)
        return ans
```

## 103. Binary Tree Zigzag Level Order Traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).\
**Method:**\
BFS. Record the level. When we are in an odd row, we need to reverse the list before saving it.\
Time complexity: O(N)\
Space complexity: O(N)
```
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        ans = []
        l = 1
        while len(q):
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if l%2==1:
                ans.append(level)
            else:
                ans.append(level[::-1])
            l += 1
        return ans
```

## 515. Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).\
**Method:**\
BFS\
Time complexity: O(N), N is the number of nodes\
Space complexity: O(N)
```
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        ans = []
        while len(q):
            size = len(q)
            max_node = float('-inf')
            for _ in range(size):
                node = q.popleft()
                max_node = max(max_node, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max_node)
        return ans
```

## 314. Binary Tree Vertical Order Traversal
Given a binary tree, return thevertical ordertraversal of its nodes' values. (ie, from top to bottom, column by column).\
If two nodes are in the same row and column, the order should be from left to right.\
**Method:**\
**In this question, we don't need to sort the values. We only need a dictionary to record the values based on the column.**\
Specifically, the key is the column number, and the values are the nodes on that column.\
We also need to track the most left column number and the most right column number.\
Time complexity: O(N)\
Space complexity: O(N), dictionary
```
class Solution(object):
    def verticalOrder(self, root):
        dic = collections.defaultdict(list)
        q = collections.deque()
        q.append((0, root))
        minCol, maxCol = 0, 0
        while len(q):
            col, node = q.popleft()
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            dic[col].append(node.val)
            if node.left is not None:
                q.append((col-1, node.left))
            if node.right is not None:
                q.append((col+1, node.right))
        
        ans = []
        for i in range(minCol, maxCol+1, 1):
              ans.append(dic[i])
        return ans
```

## 987. Vertical Order Traversal of a Binary Tree
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.\
There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.\
**Method:**\
**In this question, when there are multiple nodes at the same position, we need to sort them before saving.**\
Use a heap to save the column number, row number, and the node's value.\
Time complexity: O(NlogN)\
Space complexity: O(N)
```
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
		    return []
        h = []
        heapq.heapify(h)
        q = collections.deque()
        q.append((root, 0, 0))
        while len(q):
            size = len(q)
            for _ in range(size):
                node, row, col = q.popleft()
                heapq.heappush(h, (col, row, node.val))
                if node.left:
                    q.append((node.left, row+1, col-1))
                if node.right:
                    q.append((node.right, row+1, col+1))
        ans = []
        pre_c, c = h[0][0], []
        while len(h):
            col, row, val = heapq.heappop(h)
            if col == pre_c:
                c.append(val)
            else:
                ans.append(c)
                c = []
                pre_c = col
                c.append(val)
        if len(c):
            ans.append(c)
        return ans

```

## 133. Clone Graph
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.\
**Method:**\
Use BFS to traverse the graph.\
Need a dictionary and a set. The dictionary is to save to cloned nodes, and the set is to save the visited nodes.\
Time complexity: O(N)\
Space complexity: O(N)
```
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        dic, visited, q = {}, set(), collections.deque()
        q.append(node)
        while len(q):
            node_org = q.popleft()
            if node_org in visited:
                continue
            visited.add(node_org)
            if node_org not in dic:
                dic[node_org] = Node(node_org.val)
            for node_org_nei in node_org.neighbors:
                if node_org_nei not in dic:
                    dic[node_org_nei] = Node(node_org_nei.val)
                dic[node_org].neighbors.append(dic[node_org_nei])
                q.append(node_org_nei)
        return dic[node]
```
## 1036. Escape a Large Maze




































