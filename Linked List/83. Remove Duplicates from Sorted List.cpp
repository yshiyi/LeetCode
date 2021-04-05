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

// Method 1: using a set to save distinct values.
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        set<int> s;
        ListNode *cur = head;
        while(cur!=NULL){
            s.insert(cur->val);
            while(cur->next!=NULL && s.find(cur->next->val)!=s.end()){
                cur->next = cur->next->next;
            }
            cur = cur->next;
        }
        return head;
    }
};


// Method 2: Save all the values to a set, and transfer those distinct values to a new list.
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        ListNode *head2 = new ListNode(0);
        ListNode *cur = head2;
        set<int> s;
        while(head!=NULL){
            s.insert(head->val);
            head = head->next;
        }
        for(auto & val:s){
            ListNode *newNode = new ListNode(val);
            cur->next = newNode;
            cur = cur->next;
        }
        return head2->next;
    }
};
