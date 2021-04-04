/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int sizeA = getSize(headA), sizeB = getSize(headB);
        if(sizeA==0||sizeB==0){
            return NULL;
        }
        ListNode *curA = headA, *curB = headB;
        int totalLength = sizeA + sizeB;
        int step = 0;
        while(step<totalLength){
            if(curA == curB){
                return curA;
            }
            if(curA->next==NULL){
                curA = headB;
            }else{
                curA = curA->next;
            }
            if(curB->next==NULL){
                curB = headA;
            }else{
                curB = curB->next;
            }
            
            step++;
        }
        return NULL;
    }
    
    int getSize(ListNode *head){
        int i = 0;
        ListNode* cur = head;
        while(cur!=NULL){
            i++;
            cur = cur->next;
        }
        return i;
    }
};
