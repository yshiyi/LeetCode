<!-- GFM-TOC -->
* [Heap](#Heap)
    * [215. Kth Largest Element in an Array](#215-Kth-Largest-Element-in-an-Array)
    * [347. Top K Frequent Elements](#347-Top-K-Frequent-Elements)
    * [23. Merge K Sorted Lists](#23-Merge-K-Sorted-Lists)
    * [378. Kth Smallest Element in a Sorted Matrix](#378-Kth-Smallest-Element-in-a-Sorted-Matrix)
    * [973. K Closest Points to Origin](#973-K-Closest-Points-to-Origin)
* [BFS](#BFS)
    * [1091. Shortest Path in Binary Matrix](#1091-Shortest-Path-in-Binary-Matrix)
    * [133. Clone Graph](#133-Clone-Graph)
    * [515. Find Largest Value in Each Tree Row](#515-Find-Largest-Value-in-Each-Tree-Row)
    * [1036. Escape a Large Maze](#1036-Escape-a-Large-Maze)
    * [199. Binary Tree Right Side View](#199-Binary-Tree-Right-Side-View)
    * [314. Binary Tree Vertical Order Traversal](#314-Binary-Tree-Vertical-Order-Traversal)
    * [987. Vertical Order Traversal of a Binary Tree](#987-Vertical-Order-Traversal-of-a-Binary-Tree)

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
Constraints:\
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
Constraints:\
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
