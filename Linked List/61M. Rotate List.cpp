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
    ListNode* rotateRight(ListNode* head, int k) {
        int headSize = getSize(head);
        if(headSize<2 || k==0){
            return head;
        }
        k = k % headSize;
        ListNode* cur = head;
        while(cur->next!=NULL){
            cur = cur->next;
        }
        cur->next = head;
        
        ListNode* cur2 = head;
        for(int i=0; i<headSize-k-1;i++){
            cur2 = cur2->next;
        }
        head = cur2->next;
        cur2->next = NULL;
        
        return head;
    }
    
    int getSize(ListNode* head){
        int i = 0;
        ListNode* cur = head;
        while(cur!=NULL){
            i++;
            cur = cur->next;
        }
        return i;
    }
};
