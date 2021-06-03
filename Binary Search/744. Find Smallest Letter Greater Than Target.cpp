/*
744. Find Smallest Letter Greater Than Target
Binary Search

Description:
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
Note that the letters wrap around.
For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"

Example 3:
Input: letters = ["c","f","j"], target = "d"
Output: "f"

Example 4:
Input: letters = ["c","f","j"], target = "g"
Output: "j"

Example 5:
Input: letters = ["c","f","j"], target = "j"
Output: "c"

Constraints:
2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
*/

/*
Method 1: Similar to 162M. Find Peak Element
*/
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left = 0, right = letters.size();
        while(left < right){
            int mid = left+(right-left)/2;
            if(letters[mid]<=target){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        // In case of left==right, it means target>letters.back(). Then we need to return letters[0].
        return letters[left%letters.size()];
    }
};

/*
Method 2: If target>=letters.back(), we can simply return letters[0].
          
*/
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        if(letters.back()<=target){
            return letters[0];
        }
        int left = 0, right = letters.size()-1;  // In this problem, right=letters.size() also works.
        while(left < right){
            int mid = left + (right-left)/2;
            // This part of the code is optional.
            /* 
               if(letters[mid]<=target && (int)letters[mid+1]>target){
                  return letters[mid+1];
               }
            */
            if(letters[mid]>target){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return letters[left];
    }
};
