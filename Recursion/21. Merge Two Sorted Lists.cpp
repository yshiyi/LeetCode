// This is a recursive approach
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
    ListNode *ans = new ListNode(0);
    ListNode *cur = ans;
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        recurMerge(l1, l2);
        return ans->next;
    }
    void recurMerge(ListNode *l1, ListNode *l2){
        if(l1==NULL){
            cur->next = l2;
            return;
        }else if(l2==NULL){
            cur->next = l1;
            return;
        }
        if(l1->val <= l2->val){
            cur->next = l1;
            cur = cur->next;
            recurMerge(l1->next, l2);
        }else{
            cur->next = l2;
            cur = cur->next;
            recurMerge(l1, l2->next);
        }
    }
};
