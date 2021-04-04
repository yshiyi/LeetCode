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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *cur1 = l1, *cur2 = l2;
        ListNode *head = new ListNode(0);
        ListNode *ans = head;
        while(cur1!=NULL && cur2!=NULL){
            if(cur1->val <= cur2->val){
                head->next = cur1;
                cur1 = cur1->next;
            }else{
                head->next = cur2;
                cur2 = cur2->next;
            }
            head = head->next;
        }
        if(cur1!=NULL){
            head->next = cur1;
        }
        if(cur2!=NULL){
            head->next = cur2;
        }
        return ans->next;
    }
};
