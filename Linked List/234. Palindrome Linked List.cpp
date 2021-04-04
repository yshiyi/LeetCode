/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// Method 1: using vector
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> v;
        while(head){
            v.push_back(head->val);
            head = head->next;
        }
        if(v.size()<2){
            return true;
        }else{
            int left = 0, right = v.size()-1;
            while(left<right){
                if(v[left]!=v[right]){
                    return false;
                }
                left++;
                right--;
            }
        }
        return true;
    }
};

// Method 2: Using reverse approach
