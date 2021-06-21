## C++ and Python Reference and Algorithms
* [int vs unsigned int](#int-vs-unsigned-int)
* [Max and min int](#Max-and-min-int)
* [Generate Random Number](#Generate-Random-Number)
* [Convert between char and int](#Convert-between-char-and-int)
* [Stack and Queue](#Stack-and-Queue)
  * [Priority queue](#Priority-queue)
* [Sorting Algorithm](#Sorting-Algorithm)
  * [1. Bubble Sort](#1-Bubble-Sort)
  * [2. Quick Sort](#2-Quick-Sort)
  * [3. Merge Sort](#3-Merge-Sort)
* [Two Pointers](#Two-Pointers)
* [Sliding Window](#Sliding-Window)
* [Return {} Statement](#Return--Statement)


# int vs unsigned int
A variable defined as int can be either positive or negative.\
A variable defined as unsigned int can only be non-negative.\
When comparing signed with unsigned, the compiler converts the signed value to unsigned.\
For example,
```
/* This works fine. 
   When an unsigned int decreases from 0 to 1, it will be automatically converted to 2^32-1.
   -1 is also converted to unsigned, i.e. (unsigned)-1
*/
for (unsigned int i = v.size()-1; i != -1; --i) 

/* This works fine.
   (unsigned)-1 is equal to 2^32 - 1
*/
for (unsigned int j = v.size()-1; j < (unsigned)-1; --j)

/* This doesn't work.
   Since (unsigned)-1 is equal to 2^32 - 1, i will never be greater than that value.
*/
for (unsigned int i = v.size()-1; i > -1; --i) 
```

# Max and min int
**INT:**\
For C++: INT_MAX, INT_MIN\
For Python: 
```
float('inf'), float('-inf')
```
**Double:**\
For C++: 
```
numeric_limits<double>::max()
```

# Generate Random Number
In C++
```
// Generate a random variable between i and j, including j
rand() % (j - i + 1) + i;
```
In Python
```
randint(i, j)
```


# Convert between char and int
For C++
```
// From char to int
char c = '1';

// Method 1:
int c_int = c - '0'; // c_int = 1;
// Method 2:
int c_int2 = (int)c-48;  // c_int2 = 1; 


// From int to char:
int a = 1;
char c_a = (char)a+48;  // c_a = '1';
```
For Python
```
# From char to int
ord('a') -> 97
ord('1') -> 49

# From int to char
chr(97) -> 'a'
chr(49) -> '1'
```


# Stack and Queue
**Note:**\
In python, collections.deque() or list can contain None. On contrary, in C++, neither stack nor queue can contain nullptr.\
In C++
```
// Stack
stack<int> s;
s.push(1);
s.top(); // 1
s.pop(); // remove from top/back

//Queue
queue<int> q;
q.push(1);
q.front();
q.back();
q.pop(); // remove from bottom/front
```
In Python
```
# Stack
s = collections.deque()
s.append(1)
s[-1]
s.pop()

# Queue
q = collections.deque()
q.append(1)
q[0]
q.popleft()
```

## Priority queue
A priority_queue keeps internally a comparing function and a container object as data. Newly added elements are placed ahead of all the elements held in lower priority.
```
#include <iostream>       // std::cout
#include <queue>          // std::priority_queue

struct cmp{
  bool operator()(int i1, int i2){
     // In this case, the smaller value has higher priority and is saved on top.
     return i1 > i2;
  }
};

int main ()
{
  std::priority_queue<int> mypq;

  mypq.push(30);
  mypq.push(100);
  mypq.push(25);
  mypq.push(40);

  std::cout << "Popping out elements...";
  while (!mypq.empty())
  {
     std::cout << ' ' << mypq.top();
     mypq.pop();
  }
  std::cout << '\n';
  
  std::priority_queue<int, vector<int>, cmp> newq;
  newq.push(30); newq.push(100); newq.push(25); newq.push(40);
  std::cout << "Popping out elements...";
  while (!newq.empty())
  {
     std::cout << ' ' << newq.top();
     newq.pop();
  }
  
  return 0;
}

Output:
Popping out elements... 100 40 30 25
Popping out elements... 25 30 40 100
```
We can also use operator overloading to define the priority. So that priority_queue can decide how to store the structure object.
```
// this is an structure which implements the
// operator overloading
struct cmp()(pair<string, int> &p1, pair<string, int> &p2){
    return (p1.second > p2.second) || (p1.second==p2.second && p1.first<p2.first)
}

priority_queue<pair<string, int>, vector<pair<string, int>>, cmp> q;
```

# Sorting Algorithm
## 1. Bubble Sort
Bubble sort is the simplest technique in which we compare every element with its adjacent element and swap the elements if they are in wrong order (i.e., arr\[i\] > arr\[i+1\]). This way at the end of every iteration (called a pass), the heaviest element gets bubbled up at the end of the list.
```
C++
void bubbleSort(int * arr, int len) {
    for (int i=0; i<len-1; i++){
        for (int j=0; j<len-i-1; j++) {
            if (arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}
```
```
Python
def BubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
```
### Recursive Bubble Sort
1. Base Case: If array size is 1, return.
2. Do One Pass of normal Bubble Sort. This pass fixes last element of current subarray.
3. Recur for all elements except last of current subarray.\
```
C++
void bubbleSort(int * arr, int len) {
    if (len == 1) {return;}
    for (int j=0; j<len-1; j++) {
         if (arr[j] > arr[j+1]){
             int temp = arr[j];
             arr[j] = arr[j+1];
             arr[j+1] = temp;
         }
     }
     bubbleSort(arr, len - 1);
}
```
```
Python
def RecurBubbleSort(nums, l):
    if l == 1:
        return nums
    for i in range(l-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    RecurBubbleSort(nums, l - 1)
```

## 2. Quick Sort
Quick sort is a classcial divide-and-conquer algorithm for sorting. In detail, given a list of values to sort, the quick sort algorithm works in the following steps:
1. First, it selects a value from the list, which serves as a pivot value to divide the list into two sublists. One sublist contains all the values that are less than the pivot value, while the other sublist contains the values that are greater than or equal to the pivot value. This process is also called partitioning. The strategy of choosing a pivot value can vary. Typically, one can choose the first element in the list as the pivot, or randomly pick an element from the list.
2. After the partitioning process, the original list is then reduced into two smaller sublists. We then recursively sort the two sublists.
3. After the partitioning process, we are sure that all elements in one sublist are less or equal than any element in another sublist. Therefore, we can simply concatenate the two sorted sublists that we obtain in step 2 to obtain the final sorted list. 

The base cases of the recursion in step 2 are either when the input list is empty or the empty list contains only a single element. In either case, the input list can be considered as sorted already.\

**Time Complexity:**\
Depending on the pivot values, the time complexity of the quick sort algorithm can vary from O(NlogN) in the best case and O(N^2) in the worst case.\
In the best case, if the pivot value happens to be median value of the list, then at each partition the list would be divided into two sublists of equal size. At the end, we actually construct a balanced binary search tree (BST) out of the list. One can infer that the height of the tree would be logN, and at each level of the tree the input list would be scanned once with the complexity O(N) due to the partitioning process. As a result, the overall time complexity of the algorithm in this case would be O(NlogN).\
While in the worst case, if the pivot value happens to be the extreme value of the list, i.e. either the smallest or the biggest element in the list, then at each partition we end up with only one single sublist (i.e. the other sublist is empty). The reduction of the problem still works, but at a rather slow pace, i.e. one element at a time. The partitioning would then occur N times, and each time the partitioning scans at most N elements. Therefore, the overall time complexity of the quick sort algorithm in this case would be O(N). Actually, in this case, the quick sort algorithm ends up to be exactly as the insertion sort.\
On average, as proved mathematically, the time complexity of quick sort is O(NlogN).\
```
# Python
def quicksort(lst):
    """
    Sorts an array in the ascending order in O(n log n) time
    :param nums: a list of numbers
    :return: the sorted list
    """
    n = len(lst)
    qsort(lst, 0, n - 1)

def qsort(lst, lo, hi):
    """
    Helper
    :param lst: the list to sort
    :param lo:  the index of the first element in the list
    :param hi:  the index of the last element in the list
    :return: the sorted list
    """
    if lo < hi:
        p = partition(lst, lo, hi)
        qsort(lst, lo, p - 1)
        qsort(lst, p + 1, hi)

def partition(lst, lo, hi):
    """
    Picks the last element hi as a pivot
     and returns the index of pivot value in the sorted array
    """
    pivot = lst[hi]
    i = lo
    for j in range(lo, hi):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[hi] = lst[hi], lst[i]
    return i
```

### Quickselect Algorithm
**[347M.Top K Frequent Elements](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/347M.%20Top%20K%20Frequent%20Elements.cpp)**\
Quickselect is a selection algorithm and is typically used to solve the problems "find kth something": kth smallest, kth largest, kth most frequent, kth less frequent, etc. It is related to the quick sort sorting algorithm.\
The logic is simple, if index of partitioned element is more than k, then we recur for left part. If index is same as k, we have found the k-th smallest element and we return. If index is less than k, then we recur for right part.\
It has O(N) average time complexity and widely used in practice. It worth to note that its worth case time complexity is O(N^2), although the probability of this worst-case is negligible.
```
C++
class QuickSelect {
public:
    int quickSelect(vector<int>& nums, int left, int right, int k) {
        if (k>0 && k<= right-left+1) {
            int index = partition(nums, left, right);
            if (index - left == k-1) {
                return nums[index];
            }
            if (index - left > k - 1) {
                return quickSelect(nums, left, index - 1, k);
            }
            return quickSelect(nums, index+1, right, k-(index-left+1));
        }
        return -1;
    }

    int partition(vector<int>& nums, int left, int right) {
        int pivot = nums[right];
        int pivot_index = left;
        for (int i=left; i<right; i++) {
            if (nums[i] <= pivot) {
                swap(nums[i], nums[pivot_index]);
                pivot_index++;
            }
        }
        swap(nums[right], nums[pivot_index]);
        return pivot_index;
    }
};
```
```
Python
def partition(arr, l, r):
    pivot = arr[r];
    pivot_index = l;
    for i in range(l, r):
        if arr[i] <= pivot:
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            pivot_index += 1
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
    return pivot_index

def quickSelect(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)
        if (index - l == k - 1):
            return arr[index]
        if (index - l > k - 1):
            return quickSelect(arr, l, index-1, k)
        return quickSelect(arr, index+1, r, k-(index-l+1))
    return -1
```

## 3. Merge Sort
Merge sort algorithm is one of the classic examples of the divide-and-conquer algorithm. There are two approaches to implement the merge sort algorithm: top down or bottom up.\
**Top down approach:**\
1. In the first step, we divide the list into two sublists.  (Divide)
2. Then in the next step, we recursively sort the sublists in the previous step.  (Conquer)
3. Finally we merge the sorted sublists in the above step repeatedly to obtain the final list of sorted elements.  (Combine)

The recursion in step (2) would reach the base case where the input list is either empty or contains a single element.\
Now, we have reduced the problem down to a merge problem, which is much simpler to solve. Merging two sorted lists can be done in linear time complexity O(N), where N is the total lengths of the two lists to merge.\
```
# Python code:
def merge_sort(nums):
    # bottom cases: empty or list of a single element.
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums) / 2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1
    
    # append what is remained in either of the lists
    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])
    
    return ret
```
**Bottom up approach:**\
In the bottom up approach, we divide the list into sublists of a single element at the beginning. Each of the sublists is then sorted already. Then from this point on, we merge the sublists two at a time until a single list remains.\

**Complexity:**\
The overall time complexity of the merge sort algorithm is O(NlogN), where N is the length of the input list. To calculate the complexity, we break it down to the following steps:
1. We recursively divide the input list into two sublists, until a sublist with single element remains. This dividing step computes the midpoint of each of the sublists, which takes O(1) time. This step is repeated N times until a single element remains, therefore the total time complexity is O(N).\
2. Then, we repetitively merge the sublists, until one single list remains. As shown in the recursion tree, there are a total of N elements on each level. Therefore, it takes O(N) time for the merging process to complete on each level. And since there are a total of logN levels, the overall complexity of the merge process is O(NlogN).

Taking into account the complexity of the above two parts in the merge sort algorithm, we conclude that the overall time complexity of merge sort is O(NlogN).\
The space complexity of the merge sort algorithm is O(N), where {N}N is the length of the input list, since we need to keep the sublists as well as the buffer to hold the merge results at each round of merge process.




# Two Pointers
There are two types of approaches using two pointers technique.
1. Fast and slow pointers\
   a. Two pointers run with different speed. If they tun on a straight path, the fast pointer will first arrive at the end eventually. If there is a circle, the fast pointer will catch up with the slow pointer.
   ```
   boolean hasCycle(ListNode head) {
       ListNode fast, slow;
       fast = slow = head;
       while (fast != null && fast.next != null) {
           fast = fast.next.next;
           slow = slow.next;

           if (fast == slow) return true;
       }
       return false;
   }
   ```
      Related question:\ 
       
      **141. Linked List Cycle** [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/141.%20Linked%20List%20Cycle.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/141.%20Linked%20List%20Cycle.py)\
      **234. Palindrome Linked List** [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/234.%20Palindrome%20Linked%20List.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/234.%20Palindrome%20Linked%20List.py)\
      **82M. Remove Duplicates from Sorted List II** [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/82M.%20Remove%20Duplicates%20from%20Sorted%20List%20II.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/82M.%20Remove%20Duplicates%20from%20Sorted%20List%20II.py)
      
   b. Using this technique, we can also determine the location of the starting node of the circle.\
      Related question: 142M. Linked List Cycle II [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/142M.%20Linked%20List%20Cycle%20II.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/142M.%20Linked%20List%20Cycle%20II.py)\
   
   c. Determine the middle node of a list.\
      Related questions: 876. Middle of the Linked List [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/876.%20Middle%20of%20the%20Linked%20List.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/876.%20Middle%20of%20the%20Linked%20List.py)\
   
   d. Determine the Nth node from the end of list.\
      Related questions: 19M. Remove Nth Node From End of List [C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/19M.%20Remove%20Nth%20Node%20From%20End%20of%20List.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/19M.%20Remove%20Nth%20Node%20From%20End%20of%20List.py)

3. Left and right pointers\
   a. Binary search for a sorted array.
      ```
      int binarySearch(int[] nums, int target) {
       int left = 0; 
       int right = nums.length - 1;
       while(left <= right) {
           int mid = (right + left) / 2;
           if(nums[mid] == target)
               return mid; 
           else if (nums[mid] < target)
               left = mid + 1; 
           else if (nums[mid] > target)
               right = mid - 1;
       }
       return -1;
   }
      ```
    
   b. Two sums\
      Related question: 167. Two Sum II - Input array is sorted [C++](https://github.com/yshiyi/LeetCode/blob/main/Array/167.%20Two%20Sum%20II%20-%20Input%20array%20is%20sorted.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Array/167.%20Two%20Sum%20II%20-%20Input%20array%20is%20sorted.py)\
   c. Reverse an array\
      Related question: 344. Reverse String [C++](https://github.com/yshiyi/LeetCode/blob/main/Array/344.%20Reverse%20String.cpp), [Python](https://github.com/yshiyi/LeetCode/blob/main/Array/344.%20Reverse%20String.py)
   

# Sliding Window
Sliding window is a special method of two pointers. The basic idea is to use two different pointers to create a kind of window. Then, move this window by increasing the pointers individually. The time complexity is O(N). The basic logic is:
```
int left = 0, right = 0;
while (right < s.size()){
   window[s[right]]++;
   right++;
   
   while(window needs to shrink){
      window[s[left]]--;
      left--;
   }
}
```
**[76H. Minimum Window Substring](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/76H.%20Minimum%20Window%20Substring.cpp)**\
Description:\
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "". Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.\
Example 1:\
Input: s = "ADOBECODEBANC", t = "ABC"\
Output: "BANC"
```
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> window, need;
        for (auto& c:t) {
            need[c]++;
        }

        int left = 0, right = 0, match = 0;
        int start = 0, len = INT_MAX;
        while(right < s.size()) {
            char c = s[right];
            if (need.find(c)!=need.end()){
                window[c]++;
                // if (window[c]==1){ This doesn't work, if there are duplicate char in target string.
                if (window[c]==need[c]){
                    match++;
                }
            }
            while (match == need.size()) {
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }
                char d = s[left];
                if (need.find(d)!=need.end()){
                    if (window[d]==need[d]){
                        match--;
                    }
                    window[d]--;
                }                
                left++;
            }
            right++;
        }
        
        if (len!=INT_MAX){
            string res = s.substr(start, len+1);
            return res;
        }else{
            return "";
        }
        
    }
};
```

# Return {} Statement
In C++, return {} indicates "return an object of the function's return type initialized with an empty list-initializer". The exact behaviour depends on the returned object's type.\
```
std::string get_string() {
    return {}; // an empty string is returned
}
```












