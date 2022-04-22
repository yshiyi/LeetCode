* [Two Sum](#two-sum)
* [Longest Repeated Subarray](#Longest-Repeated-Subarray)
* [29. Divide Two Integers](#29-Divide-Two-Integers)
* [Simplified XML Validator](#Simplified-XML-Validator)
* [66. Plus One](#66-Plus-One)
* [238. Product of Array Except Self](#238-Product-of-Array-Except-Self)
* [146. LRU Cache](#146-LRU-Cache)
* [69. Sqrt(x)](#69-sqrtx)
* [13. Roman to Integer](#13-Roman-to-Integer)
* [Knapsack](#Knapsack)
* [208. Implement Trie (Prefix Tree)](#208-Implement-Trie-Prefix-Tree)


# Two Sum
Output all possible solutions.\
Example:\
Input: \[4,4,4,1,1\], target = 5\
Output: \[4,1\], \[4,1\], \[4,1\], \[4,1\], \[4,1\], \[4,1\]\
**Method:**\
Notice, there are duplicate solutions. Therefore, we need to use Counter to count all the appearances of each element.\
Then use two pointer to sweep the keys from the two ends.
```
import collections
class Solution(object):
    def twoSum(self, nums, target):
        count = collections.Counter(nums)
        vals = list(count.keys())
        vals.sort()
        p1, p2 = 0, len(vals)-1
        ans = []
        while p1 < p2:
            _sum = vals[p1] + vals[p2]
            if _sum==target:
                for _ in range(count[vals[p1]]*count[vals[p2]]):
                    ans.append([vals[p1], vals[p2]])
                p2 -= 1
            elif _sum > target:
                p2 -= 1
            else:
                p1 += 1
        return ans
```


# Longest Repeated Subarray
Example:\
Input: \[2,2,2,2,2,1,1,4,4\]\
Output: \[2,2,2,2,2\]\
**Method:**\
At the end of the sript, remember to check the length of _window, in case the last window is the longest.
```
class Solution(object):
    def longestRepeat(self, nums):
        if len(nums)==1:
            return nums
        left, right = 0, 1
        max_size, _window = 0, [nums[0]]
        ans = []
        while right < len(nums):
            if nums[right]==nums[right-1]:
                _window.append(nums[right])
                right += 1
            else:
                if len(_window)>max_size:
                    ans = _window
                    max_size = len(_window)
                _window = [nums[right]]
                right += 1
        if len(_window)>max_size:
            ans = _window
        return ans

sol = Solution()
nums = [4,4,4,3,2,2,2,2,1,1,1,1,1,1]
print(sol.longestRepeat(nums))
```

# 29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.\
The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.\
Return the quotient after dividing dividend by divisor.\
**Method:**\
Two pointers. Need to check the signs of both dividend and divisor.\
```
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        left, right = -sys.maxint, sys.maxint
        if (divisor>0 and dividend>0) or (divisor<0 and dividend<0):
            sign = 1
        else:
            sign = -1
        while left < right:
            mid = (left + right)//2
            if mid*abs(divisor)<=abs(dividend) and (mid+1)*abs(divisor)>abs(dividend):
                res = mid*sign
                break
            elif mid*abs(divisor)>abs(dividend):
                right = mid
            else:
                left = mid + 1

        res = min(res, 2147483647)
        res = max(res, -2147483648)
        return res
```

# Simplified XML Validator
The start-tag and end-tag elements must be correctly nested, with none missing and none overlapping. \
For example, text <a> text</a>, <a>text<b>other text</b></a> are valid, <a>text<b>other text</a></b> is not.\
The goal of this question is to simulate an xml validator. \
We will give you sample xml text and you should output wheter the text is valid xml or not.\
```
import collections
class Solution(object):
    def validXML(self, text):
        stack = collections.deque()
        i = 0
        while i<len(text):
            if text[i]=="<":
                valid, tag = self.helper(text[i:])
                if not valid:
                    return False
		#tags cannot be empty
                if tag=="" or tag=="/":
                    return False
		#If we find a closing tag </abc>
                if tag[0]=="/":
		    #if stack is empty, that means there was no opening tag, return false
                    if len(stack)==0:
                        return False
		    #if stack top is 'abc' but our closing tag is 'xyz', return False
                    if stack[-1]!=tag[1:]:
                        return False
		    #if there is a match to our closing tag then pop it from stack
                    stack.pop()
                else:
		     #if this is the opening tag then add it to stack
                    stack.append(tag)
		#we increment i to tag length plus 2 to add <> to the legth of i
                i += len(tag)+2
            elif text[i]==">":
		#if there is a random > in text then return false
                return False
            else:
                i += 1
        if len(stack):
	    #if we never found a closing tag to one of our opening tags
            return False
        return True
    
    def helper(self, text):
        tag = ""
        for i in range(1, len(text)):
            if text[i]=="<":
                #text = <<abc>
                return False, -1
            if text[i]==">":
		#Completes the tag <abc>
                return True, tag
            tag += text[i]
        return True, tag


sol = Solution()
text = "<a>text<b>other text</b></b>"
print(sol.validXML(text))
```

# 66. Plus One
You are given a large integer represented as an integer array digits, where each digits\[i\] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.\
Increment the large integer by one and return the resulting array of digits.\
**Method:**\
We need to check the value of carry at the end of script.
```
class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
        if carry == 1:
            return [1]+digits
        else:
            return digits
```

# 238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer\[i\] is equal to the product of all the elements of nums except nums\[i\].\
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.\
You must write an algorithm that runs in O(n) time and without using the division operation.\
**Method:**\
Sweep the array twice.\
First time, sweep from left and record the product until n-1.\
Second time, sweep from right and keep tracking the product from the right.
```
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_left = [1]
        for i in range(len(nums)-1):
            product_left.append(product_left[-1]*nums[i])
        ans = [0] * len(nums)
        product_right=1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = product_left[i] * product_right
            product_right *= nums[i]
        return ans
```

# 146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.\
Implement the LRUCache class:
1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
2. int get(int key) Return the value of the key if the key exists, otherwise return -1.
3. void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
**Method:**\

```
class Node(object):
    def __init__(self, k, v, next=None, prev=None):
        self.key = k
        self.value = v
        self.next = next
        self.prev = prev

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.defaultdict(Node)
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic.keys():
            return -1
        self.removeNode(self.dic[key])
        self.addNode(self.dic[key])
        
        return self.dic[key].value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic.keys():
            self.removeNode(self.dic[key])
        self.dic[key] = Node(key, value)
        self.addNode(self.dic[key])
        if len(self.dic) > self.cap:
            node = self.head.next
            self.removeNode(node)
            self.dic.pop(node.key, None)
    
    def removeNode(self, node):
        tmp1 = node.prev
        tmp2 = node.next
        tmp1.next = node.next
        tmp2.prev = node.prev
    
    def addNode(self, node):
        tmp1 = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        tmp1.next = node
        node.prev = tmp1
```

# 69. Sqrt(x)
Given a non-negative integer x, compute and return the square root of x.\
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.\
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.\
Constraints:\
0 <= x <= 231 - 1\
**Method:**\
Note: we need to return left at the end.
```
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        while left < right:
            mid = (left+right)//2
            if mid**2<=x and (mid+1)**2>x:
                return mid
            elif mid**2>x:
                right = mid
            else:
                left = mid + 1
        return left
```

# 13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.\
Symbol       Value\
I             1\
V             5\
X             10\
L             50\
C             100\
D             500\
M             1000\
Example:\
Input: s = "MCMXCIV"\
Output: 1994\
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.\
**Method:**\
In most of cases, the string is in non-ascending order.\
We only need to find the letters that are smaller than its next one.\
Time complexity: O(N)\
Space complexity: O(1)\
```
class Solution(object):
    def romanToInt(self, s):
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if len(s)==1:
            return dic[s[0]]
        ans = 0
        i = 0
        while i < len(s)-1:
            if dic[s[i]]>=dic[s[i+1]]:
                ans += dic[s[i]]
                i += 1
            else:
                ans += dic[s[i+1]] - dic[s[i]]
                i += 2
        if i == len(s)-1:
            ans += dic[s[i]]
        return ans
```

# Knapsack
给你⼀个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。其中第 i 个物品的重量为 wt\[i\]，价值为 val[i]，现在让你⽤这个背包装物品，最多能装的价值是多少？\
Example:\
N = 3, W = 4\
wt = \[2, 1, 3\]\
val = \[4, 2, 3\]\
**Method:**\
This is a dynamic programming problem.\
First, we need to determine the states and actions.\
There are two states: the number of objects, and weight remain in the bagpack.\
Two actions: put object i into the bag, and not put object i into the bag.\

Second, we need to define a transition function.\
The optimal value in each state dp\[n\]\[w\] should be the maximum of outcome of two actions.\
1. If we put the object n into the bag, what is the optimal value?
   val\[n-1\] + dp\[n-1\]\[w-wt\[n-1\]\], object n's value + the optimal value that put n-1 objects with w-wt[n-1] weight\
2. If we don't put th object n into the bag.
   dp\[n-1\]\[w\], the optimal value that put n-1 objects with w weight\
3. Corner case. if w-wt\[n-1\]<0.
   It means we can't put object n into the bag, the dp\[n\]\[w\] = dp\[n-1\]\[w\]\
```
class Solution(object):
    def knapSack(self, N, W, wt, val):
        dp = [[0] * (W+1) for _ in range(N+1)]
        for n in range(1, N+1):
            for w in range(1, W+1):
                if w - wt[n-1] < 0:
                    dp[n][w] = dp[n-1][w]
                else:
                    dp[n][w] = max(dp[n-1][w], val[n-1] + dp[n-1][w-wt[n-1]])
        return dp[N][W]

sol = Solution()
N, W = 3, 4
wt = [2, 1, 3]
val = [4, 2, 3]
print(sol.knapSack(N, W, wt, val))
[[0, 0, 0, 0, 0], 
 [0, 0, 4, 4, 4], 
 [0, 2, 4, 6, 6], 
 [0, 2, 4, 6, 6]]
```

# 208. Implement Trie (Prefix Tree)
```
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.is_word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for letter in word:
            cur = cur.children.get(letter)
            if cur is None:
                return False
        return cur.is_word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for letter in prefix:
            cur = cur.children.get(letter)
            if cur is None:
                return False
        return True
```
