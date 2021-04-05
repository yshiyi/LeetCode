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

// Method 1: Save all duplicated elements to a set. Then save all elements not included in the set to a new list.
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        ListNode *cur = head;
        set<int> s;
        while(cur!=NULL && cur->next!=NULL){
            if(cur->val == cur->next->val){
                s.insert(cur->val);
            }
            cur = cur->next;
        }
        ListNode *head2 = new ListNode(0);
        ListNode *ans = head2;
        cur = head;
        while(cur!=NULL){
            if(s.find(cur->val)==s.end()){
                ListNode *newNode = new ListNode(cur->val);
                head2->next = newNode;
                head2 = head2->next;
            }
            cur = cur->next;
        }
        return ans->next;
    }
};


// Method 2: Using two pointers
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        ListNode *head2 = new ListNode(NULL);
        head2->next = head;
        ListNode *cur1 = head2, *cur2 = head;
        while(cur2!=NULL){
            if(cur2->next!=NULL && cur2->val==cur2->next->val){
                while(cur2->next!=NULL && cur2->val==cur2->next->val){
                    cur2 = cur2->next;
                }
                cur1->next = cur2->next;
            }else{
                cur1 = cur1->next;
            }
            cur2 = cur2->next;
        }
        return head2->next;
    }
};
