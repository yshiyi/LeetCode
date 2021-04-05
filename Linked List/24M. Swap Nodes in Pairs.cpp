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
// Method 1: Using one pointer.
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        ListNode *cur1 = head;
        ListNode *head2 = new ListNode(0);
        ListNode *cur2 = head2;
        ListNode *tmp;
        
        while(cur1!=NULL && cur1->next!=NULL){
            tmp = cur1->next->next;
            cur2->next = cur1->next;
            cur2 = cur2->next;
            cur2->next = cur1;
            cur2 = cur2->next;
            cur2->next = tmp;
            cur1 = tmp;
        }
        return head2->next;
    }
};


// Method 2: Recursive method.
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        
        ListNode *head2 = head->next, *tmp = head->next->next;
        head2->next = head;
        head->next = swapPairs(tmp);
        
        return head2;
    }
};
