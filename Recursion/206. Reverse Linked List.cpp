// This is a recursive solution.
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
        if(head==NULL){
            return head;
        }
        ListNode *head2 = new ListNode(0);
        head2 = recurReverse(head, head2);
        return head2->next;
    }
    ListNode* recurReverse(ListNode* head, ListNode* head2){
        if(head==NULL){
            return head;
        }
        ListNode* temp1 = head->next;
        ListNode* temp2 = head2->next;
        head2->next = head;
        head->next = temp2;
        recurReverse(temp1, head2);
        return head2;
    }
};

// Method 2:
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        ListNode* last = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return last;
    }
};
