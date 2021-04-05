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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==1 || getSize(head)<k){
            return head;
        }
        // Note: we must define head2 as a null pointer, otherwise it will course problem when we check cur->next!=NULL.
        ListNode *head2=nullptr, *tmp;
        int counter = 0;
        while(counter < k){
            tmp = head->next;
            head->next = head2;
            head2 = head;
            head = tmp;
            counter++;
        }
        ListNode *cur=head2;
        while(cur->next!=NULL){
            cur = cur->next;
        }
        cur->next = reverseKGroup(head, k);
        return head2;
    }
    
    int getSize(ListNode* head){
        int size = 0;
        while(head!=NULL){
            size++;
            head = head->next;
        }
        return size;
    }
};
