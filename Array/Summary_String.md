# String
<!-- GFM-TOC -->
* [Leetcode String](#String)
    * [1. Introduction to String](#1-Introduction-to-String)
       * [1.1 Compare Function](#11-Compare-Function)
       * [1.2 Immutable or Mutable](#12-Immutable-or-Mutable)
       * [1.3 Extra Operation](#13-Extra-Operation)
       * [1.4 Time Complexity](#14-Time-Complexity)
    * [2. Stack]
       * [67. Add Binary](#67-Add-Binary)
    * [3. Two Pointers]
       * [28. Implement strStr()](#28-Implement-strStr)
       * [344. Reverse String](#344-Reverse-String)
       * [9. Palindrome Number](#9-Palindrome-Number)
       * [167. Two Sum II](#167-Two-Sum-II)
       * [209M. Minimum Size Subarray Sum](#209M-Minimum-Size-Subarray-Sum)
    * [4. Hash Table]
       * [242. Valid Anagram](#242-Valid-Anagram)
       * [409. Longest Palindrome](#409-Longest-Palindrome)
       * [205. Isomorphic Strings](#205-Isomorphic Strings)
    * [5. Others]
       * [14. Longest Common Prefix](#14-Longest-Common-Prefix)
       * [696. Count Binary Substrings](#696-Count-Binary-Substrings)
       * [561. Array Partition I](#561-Array-Partition-I)
       * [119. Pascal's Triangle II](#119-Pascals-Triangle-II)
       * [151M. Reverse Words in a String](#151M-Reverse-Words-in-a-String)
       * [557. Reverse Words in a String III](#557-Reverse-Words-in-a-String-III)
<!-- GFM-TOC -->


# 1. Introduction to String
## 1.1 Compare Function
Use "==" to compare two strings in both C++ and python.
```
int main() {
    string s1 = "Hello World";
    cout << "s1 is \"Hello World\"" << endl;
    string s2 = s1;
    cout << "s2 is initialized by s1" << endl;
    string s3(s1);
    cout << "s3 is initialized by s1" << endl;
    // compare by '=='
    cout << "Compared by '==':" << endl;
    cout << "s1 and \"Hello World\": " << (s1 == "Hello World") << endl; // 1
    cout << "s1 and s2: " << (s1 == s2) << endl; // 1
    cout << "s1 and s3: " << (s1 == s3) << endl; // 1
    // compare by 'compare'
    cout << "Compared by 'compare':" << endl;
    cout << "s1 and \"Hello World\": " << !s1.compare("Hello World") << endl; // 1
    cout << "s1 and s2: " << !s1.compare(s2) << endl; // 1
    cout << "s1 and s3: " << !s1.compare(s3) << endl; // 1
}
```
## 1.2 Immutable or Mutable
Immutable means that you can't change the content of the string once it's initialized.\
In C++ and python, the string is mutable.
```
#include <iostream>

int main() {
    string s1 = "Hello World";
    s1[5] = ',';
    cout << s1 << endl;  // Hello,World
}
```
## 1.3 Extra Operation
Concatenate, find and substr
```
#include <iostream>

int main() {
    string s1 = "Hello World";
    // 1. concatenate
    s1 += "!";
    cout << s1 << endl; // Hello World!
    // 2. find
    cout << "The position of first 'o' is: " << s1.find('o') << endl; // 4
    cout << "The position of last 'o' is: " << s1.rfind('o') << endl; // 7
    // 3. get substr
    cout << s1.substr(6, 5) << endl; // World
}
```
## 1.4 Time Complexity
If the length of the string is N, the time complexity of both finding operation and substring operation is O(N).\
Never forget to take the time complexity of built-in operations into consideration when you compute the time complexity for your solution.


# 2. Stack
When we are asked to examine the elements from right to left, we should consider to use stack which is a FILO (first-in last-out) context.
## 445M. Add Two Numbers II
[C++](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/445M.%20Add%20Two%20Numbers%20II.cpp)\
[Python](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/445M.%20Add%20Two%20Numbers%20II.py)

## 67. Add Binary
**Description:**\
Given two binary strings a and b, return their sum as a binary string.\
Note:\
C++: use (int)c-48 to convert char to int, and use (char)(i + 48) to convert int to char.\
Python: use ord(char)-48 to convert char to int, and use str(i) to convert int to char.\
        The stack structure in python can be represeted as a list or a deque() from collections.\
        deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.\
```
stack1 = []
stack1.append()
stack1.pop()
from collections import deque
stack2 = deque()
stack2.append()
stack2.pop()
```
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/67.%20Add%20Binary.cpp)
```
class Solution {
public:
    string addBinary(string a, string b) {
        stack<int> sa, sb;
        for(auto& c:a){
            sa.push((int)c-48);
        }
        for(auto& c:b){
            sb.push((int)c-48);
        }
        int carry = 0, sum;
        stack<int> s_sum;
        while(sa.size()>0 && sb.size()>0){
            sum = sa.top() + sb.top() + carry;
            if(sum < 2){
                s_sum.push(sum);
                carry = 0;
            }else if(sum==2){
                s_sum.push(0);
                carry = 1;
            }else{
                s_sum.push(1);
                carry = 1;
            }
            sa.pop(); sb.pop();
        }
        while(sa.size()>0){
            sum = sa.top() + carry;
            if(sum < 2){
                s_sum.push(sum);
                carry = 0;
            }else if(sum==2){
                s_sum.push(0);
                carry = 1;
            }else{
                s_sum.push(1);
                carry = 1;
            }
            sa.pop();
        }
        while(sb.size()>0){
            sum = sb.top() + carry;
            if(sum < 2){
                s_sum.push(sum);
                carry = 0;
            }else if(sum==2){
                s_sum.push(0);
                carry = 1;
            }else{
                s_sum.push(1);
                carry = 1;
            }
            sb.pop();
        }
        if(carry==1){
            s_sum.push(carry);
        }
        string res="";
        while(s_sum.size()>0){
            res += (char)(s_sum.top() + 48);
            s_sum.pop();
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/67.%20Add%20Binary.py)
```
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sa, sb, s_sum = [], [], [];
        for char in a:
            sa.append(ord(char)-48)
        for char in b:
            sb.append(ord(char)-48)
        carry = 0
        while len(sa)>0 and len(sb)>0:
            sum = sa[-1] + sb[-1] + carry
            if sum < 2:
                s_sum.append(sum)
                carry = 0
            elif sum == 2:
                s_sum.append(0)
                carry = 1
            else:
                s_sum.append(1)
                carry = 1
            sa.pop()
            sb.pop()
        while len(sa)>0:
            sum = sa[-1] + carry
            if sum < 2:
                s_sum.append(sum)
                carry = 0
            elif sum == 2:
                s_sum.append(0)
                carry = 1
            else:
                s_sum.append(1)
                carry = 1
            sa.pop()
        while len(sb)>0:
            sum = sb[-1] + carry
            if sum < 2:
                s_sum.append(sum)
                carry = 0
            elif sum == 2:
                s_sum.append(0)
                carry = 1
            else:
                s_sum.append(1)
                carry = 1
            sb.pop()
        if carry == 1:
            s_sum.append(1)
        
        res = ""
        while len(s_sum) > 0:
            res += str(s_sum[-1])
            s_sum.pop()
        return res
```


# 3. Two Pointers]
## 28. Implement strStr
**Description:**\
Implement strStr().\
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.\
Clarification:\
What should we return when needle is an empty string? This is a great question to ask during an interview.\
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().\
**Method:**\
Sliding window, or string.find(substr)\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/28.%20Implement%20strStr().cpp)
```
// Method 1: Sliding Window
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size()==0){
            return 0;
        }else if(haystack.size()==0){
            return -1;
        }
        int right = 0, left = 0;
        unordered_map<char, int> m_needle;
        for(auto& c:needle){
            m_needle[c]++;
        }
        unordered_map<char, int> m_window; int match = 0;
        while(right < haystack.size()){
            char c = haystack[right];
            if(m_needle.find(c)!=m_needle.end()){
                m_window[c]++;
                if(m_window[c]==m_needle[c]){
                    match++;
                }
            }
            right++;
            while(match==m_needle.size()){
                char cl = haystack[left];
                if(m_window.find(cl)!=m_window.end()){
                    m_window[cl]--;
                    if(m_window[cl]<m_needle[cl]){
                        match--;
                    }
                }
                string str_window = haystack.substr(left, right-left);
                if(str_window == needle){
                    return left;
                }
                left++;
            }
            
        }
        return -1;
    }
};


// Method 2: string.find(substr) searches the string for the first occurrence of the sequence specified by its        arguments. 
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty()) return 0;
        return haystack.find(needle);
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/28.%20Implement%20strStr().py)
```
# Method 1: string.find(substr)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0;
        return haystack.find(needle)


'''
Method 2: Sliding Window
          Note: 1. create the dictionaries as defaultdic(int)
                2. check if key exists without updating the value, use if key in Dic
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        Dic_needle, Dic_window = defaultdict(int), defaultdict(int)
        match, r, l = 0, 0, 0
        for c in needle:
            Dic_needle[c] += 1
        
        while r < len(haystack):
            c = haystack[r]
            if c in Dic_needle:
                Dic_window[c] += 1
                if Dic_window[c] == Dic_needle[c]:
                    match += 1
            r += 1
            while match == len(Dic_needle):
                if haystack[l:r] == needle:
                    return l
                cl = haystack[l]
                if cl in Dic_needle:
                    Dic_window[cl] -= 1
                    if Dic_window[cl] < Dic_needle[cl]:
                        match -= 1
                l += 1
        
        return -1
```

## 344. Reverse String
**Description:**\
Write a function that reverses a string. The input string is given as an array of characters s.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/344.%20Reverse%20String.cpp)
```
class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0, right = s.size() - 1;
        while(left < right){
            swap(s[left], s[right]);
            right--;
            left++;
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/344.%20Reverse%20String.py)
```
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
```

## 9. Palindrome Number
**Description:**\
Given an integer x, return true if x is palindrome integer.\
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.\
**Method:**\
Two pointers. For python, to read a list from right to left, we can use x\[::-1\].\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/9.%20Palindrome%20Number.cpp)
```
class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0){
            return false;
        }
        string xs = to_string(x);
        int left = 0, right = xs.size()-1;
        while(left<right){
            if(xs[left]!=xs[right]){
                return false;
            }
            left++; right--;
        }
        return true;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/9.%20Palindrome%20Number.py)
```
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xs = str(x)
        return xs[::-1]==xs
```

## 167. Two Sum II
**Description:**\
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.\
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer\[0\] < answer\[1\] <= numbers.length.\
You may assume that each input would have exactly one solution and you may not use the same element twice.\
**Method:**\
Sort the array first. Use two pointers to swap through the array from right and left seperately.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/167.%20Two%20Sum%20II%20-%20Input%20array%20is%20sorted.cpp)
```
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size()-1;
        vector<int> res;
        while(left<right){
            int sum = numbers[left] + numbers[right];
            if(sum==target){
                res.push_back(left+1);
                res.push_back(right+1);
                break;
            }else if(sum>target){
                right--;
            }else if(sum<target){
                left++;
            }
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/167.%20Two%20Sum%20II%20-%20Input%20array%20is%20sorted.py)
```
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while left < right:
            sum = numbers[right] + numbers[left]
            if sum == target:
                return [left+1, right+1]
            if sum > target:
                right -= 1
            if sum < target:
                left += 1
        return
```

## 209M. Minimum Size Subarray Sum
**Description:**\
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray \[numsl, numsl+1, ..., numsr-1, numsr\] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.\
**Method:**\
Sliding window.\
Note: INT_MAX for c++, float('inf') for python.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/209M.%20Minimum%20Size%20Subarray%20Sum.cpp)
```
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if(nums[0]>=target){
            return 1;
        }
        
        int left=0, right=1;
        int sum = nums[0], min_len = INT_MAX;
        while(right < nums.size()){
            sum = sum + nums[right];
            while(sum>=target){
                min_len = min(min_len, right-left+1);
                sum = sum - nums[left];
                left++;
            }
            right++;
        }
        if(min_len==INT_MAX){
            return 0;
        }else{
            return min_len;
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/209M.%20Minimum%20Size%20Subarray%20Sum.py)
```
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = float('inf')
        if nums[0]>=target:
            return 1
        left, right, ans = 0, 1, nums[0]
        while right < len(nums):
            ans += nums[right]
            while(ans >= target):
                min_len = min(min_len, right - left + 1)
                ans -= nums[left]
                left += 1
            right += 1
        if min_len==float('inf'):
            return 0
        else:
            return min_len
```


# 4. Hash Table
## 242. Valid Anagram
**Desciption:**\
Given two strings s and t, return true if t is an anagram of s, and false otherwise.\
**Method:**\
Use a hash table to count the appearances of characters.\
For python, we can also use collections.Counter which returns a dictionary.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/242.%20Valid%20Anagram.cpp)
```
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> ms;
        for(auto& c:s){
            ms[c]++;
        }
        for(auto& c:t){
            if(ms.find(c)==ms.end()){
                return false;
            }else{
                ms[c]--;
            }
        }
        for(auto& key:ms){
            if(key.second!=0){
                return false;
            }
        }
        return true;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/242.%20Valid%20Anagram.py)
```
# Method 1:
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Dis_s = collections.Counter(s)
        for c in t:
            if c in Dis_s:
                Dis_s[c] -= 1
            else:
                return False
        for c in Dis_s:
            if Dis_s[c] != 0:
                return False
        return True
        
# Method 2:
class Solution(object):
    def isAnagram(self, s, t):
        Dis_s = collections.Counter(s)
        Dis_t = collections.Counter(t)
        if Dis_s == Dis_t:
            return True
        else:
            return False
```

## 409. Longest Palindrome
**Description:**\
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.\
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.\
**Method:**\
Any characters with even appearances can be added to the answer. We need to check the ones with odd appearances.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/409.%20Longest%20Palindrome.cpp)
```
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> ms;
        for(auto& c:s){
            ms[c]++;
        }
        int flag = 0, ans = 0;
        for(auto& key:ms){
            if(key.second%2==0){
                ans += key.second;
            }else{
                ans += key.second - 1;
                flag = 1;
                /*
                if(ans%2==0){
                  ans += 1;
                }
                */
            }
        }
        if(flag){
            return ans+1;
        }else{
            return ans;
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/409.%20Longest%20Palindrome.py)
```
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
```

## 205. Isomorphic Strings
**Description:**\
Given two strings s and t, determine if they are isomorphic.\
Two strings are isomorphic if the characters in s can be replaced to get t.\
All occurrences of a character must be replaced with another character while preserving the order of characters. \
No two characters may map to the same character but a character may map to itself.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/205.%20Isomorphic%20Strings.cpp)\
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/205.%20Isomorphic%20Strings.py)

# 5. Others
## 14. Longest Common Prefix
**Description:**\
Write a function to find the longest common prefix string amongst an array of strings.\
If there is no common prefix, return an empty string "".\
**Method:**\
Use the characters in the first string as a reference, and compare each of them with other strings sequentially.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/14.%20Longest%20Common%20Prefix.cpp)
```
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0){
            return "";
        }
        string ans = "";
        for (int i=0; i< strs[0].size(); i++){
            for(int j=1; j<strs.size();j++){
                if(i==strs[j].size() || strs[0][i]!=strs[j][i]){
                    return ans;
                }
            }
            ans += strs[0][i];
        }
        return ans;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/14.%20Longest%20Common%20Prefix.py)
```
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        ans = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i==len(strs[j]) or strs[j][i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans
```

## 696. Count Binary Substrings
**Description:**\
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.\
Substrings that occur multiple times are counted the number of times they occur.\
**Hint:**\
How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/696.%20Count%20Binary%20Substrings.cpp)
```
class Solution {
public:
    int countBinarySubstrings(string s) {
        vector<int> v;
        int i = 0, c = 0;
        while(i<s.size()){
            while(i<s.size() && s[i]=='0'){
                c++;
                i++;
            }
            if(c!=0){
                v.push_back(c);
                c = 0;
            }
            while(i<s.size() && s[i]=='1'){
                c++;
                i++;
            }
            if(c!=0){
                v.push_back(c);
                c = 0;
            }
        }
        int ans = 0;
        for(int j=0; j<v.size()-1; j++){
            ans += min(v[j], v[j+1]);
        }
        return ans;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/696.%20Count%20Binary%20Substrings.py)
```
# Method 1:
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, c = 0, 0
        l = []
        while i<len(s):
            while i<len(s) and s[i] == '0':
                c += 1
                i += 1
            if c != 0:
                l.append(c)
                c = 0
            while i<len(s) and s[i] == '1':
                c += 1
                i += 1
            if c!= 0:
                l.append(c)
                c = 0
        
        ans = 0
        for j in range(len(l)-1):
            ans += min(l[j], l[j+1])
        return ans

# Method 2:
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        l = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                l[-1] +=1
            else:
                l.append(1)
        
        ans = 0
        for j in range(len(l)-1):
            ans += min(l[j], l[j+1])
        return ans
```

## 561. Array Partition I
**Description:**\
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.\
**Method:**\
Minimum element gets add into the result in sacrifice of maximum element.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/561.%20Array%20Partition%20I.cpp)
```
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int sum = 0;
        for(int i=1;i<nums.size();i+=2){
            sum += min(nums[i], nums[i-1]);
        }
        return sum;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/561.%20Array%20Partition%20I.py)
```
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort();
        sum = 0
        for i in range(1, len(nums), 2):
            sum += min(nums[i], nums[i-1])
        return sum
```

## 119. Pascal's Triangle II
**Description:**\
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.\
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:\
1\
11\
121\
1331\
14641\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/119.%20Pascal's%20Triangle%20II.cpp)
```
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result;
        result.resize(rowIndex + 1);
        result[0] = 1;
        result[rowIndex] = 1;
        for (int i = 1; i <= rowIndex; ++i) {
            result[i] = 1;
            for (int j = i - 1; j > 0; --j) {
                result[j] = result[j] + result[j - 1];
            }
        }
        return result;
      }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/119.%20Pascal's%20Triangle%20II.py)
```
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        ans.append(1)
        for i in range(1, rowIndex+1):
            ans.append(1)
            for j in range(i-1, 0, -1):
                ans[j] = ans[j] + ans[j-1]
        
        return ans
```

## 151M. Reverse Words in a String
**Description:**\
Given an input string s, reverse the order of the words.\
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.\
Return a string of the words in reverse order concatenated by a single space.\
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.\
**Method:**\ 
Note:\
For C++, use isspace() to check if the character is a space.\
For Python, use string.split() to retrieve the words within the string.\
There are two scenarios that need to be considered:
1. If s\[i\] is not a space, then we save it to a string, word;
2. If s\[i\] is a space, then we need to check the size of word.
   If word.size() is not 0, it means we have save a complete word and we save it to a vector.\
   If we reach the end of string and the last character is not a space, we need to save the last word to the vector.\

[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/151M.%20Reverse%20Words%20in%20a%20String.cpp)
```
class Solution {
public:
    string reverseWords(string s) {
        vector<string> v;
        int right=0;
        string word="";
        while(right<s.size()){
            if(!isspace(s[right])){
                word += s[right];
                if(right==s.size()-1){
                    v.push_back(word);
                }
            }else{
                if(word.size()!=0){
                    v.push_back(word);
                    word = "";
                }
            }
            right++;
        }

        string ans;
        for(int i=v.size()-1;i>-1;i--){
            ans += v[i] +" ";
        }
        ans.pop_back();
        return ans;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/151M.%20Reverse%20Words%20in%20a%20String.py)
```
# Method: using string.split()
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = s.split()
        ans = ""
        for i in range(len(sl)-1, -1, -1):
            ans += sl[i] + " "

        return ans[:-1]
```

## 557. Reverse Words in a String III
**Description:**\
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.\
**Example:**\
Input: s = "Let's take LeetCode contest"\
Output: "s'teL ekat edoCteeL tsetnoc"\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/557.%20Reverse%20Words%20in%20a%20String%20III.cpp)
```
// Method: using replace(start, # of char, newString)
class Solution {
public:
    string reverseWords(string s) {
        if(s.size()==1){
            return s;
        }
        int start = 0;
        for(int i=0; i<s.size()+1; i++){
            if(isspace(s[i])){
                s.replace(start, i-start, reverseString(s.substr(start, i-start)));
                start = i+1;
            }
            if(i==s.size()){
                s.replace(start, i-start, reverseString(s.substr(start, i-start)));
            }
        }
        return s;
    }
    string reverseString(string substr){
        int left = 0, right = substr.size()-1;
        while(left < right){
            swap(substr[left], substr[right]);
            left++; right--;
        }
        return substr;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/557.%20Reverse%20Words%20in%20a%20String%20III.py)
```
# Method 1: using two pointers
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        for i, c in enumerate(s):
            if c.isspace():
                newStr = self.reverseStr(s[start:i])
                s = s[0:start] + newStr + s[i:]
                start = i+1
            if i==len(s)-1:
                newStr = self.reverseStr(s[start:i+1])
                s = s[0:start] + newStr
        return s
    
    def reverseStr(seld, s):
        return s[::-1]

      
'''
Method 2: Using string.split() to split a string into a list where each word is a list item
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = [x[::-1] for x in s.split()]
        ans = ""
        for str in sl:
            ans += str + " "
        return ans[:-1]
```






