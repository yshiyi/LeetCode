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
    ListNode* oddEvenList(ListNode* head) {
        if(head==NULL || head->next==NULL || head->next->next==NULL){
            return head;
        }
        ListNode *cur1 = head, *cur2 = head;
        int counter = 1;
        while(cur2!=NULL&&cur2->next!=NULL){
            if(counter%2==0){
                // Take out node
                ListNode *tmp = cur2->next;
                cur2->next = cur2->next->next;
                // Incert node
                tmp->next = cur1->next;
                cur1->next = tmp;
                // Move the first pointer
                cur1 = cur1->next;
            }else{
                cur2 = cur2->next;
            }
            counter++;
        }
        return head;
    }
};
