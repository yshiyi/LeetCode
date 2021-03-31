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
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *newHead = nullptr;
        ListNode *cur;
        ListNode *tmp;
        cur = head;
        while(cur!=NULL){
            tmp = cur->next;
            cur->next = newHead;
            newHead = cur;
            cur = tmp;
        }
        return newHead;
    }
};
