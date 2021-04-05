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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0, sum, val;
        ListNode *head2 = new ListNode(0);
        ListNode *ans = head2;
        while(l1!=NULL && l2!=NULL){
            sum = l1->val + l2->val + carry;
            if(sum >= 10){
                val = sum - 10;
                carry = 1; 
            }else{
                val = sum;
                carry = 0;
            }
            ListNode *newNode = new ListNode(val);
            head2->next = newNode;
            head2 = head2->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        if(l1!=NULL){
            while(l1!=NULL){
                sum = l1->val + carry;
                if(sum >= 10){
                    val = sum - 10;
                    carry = 1; 
                }else{
                    val = sum;
                    carry = 0;
                }
                ListNode *newNode = new ListNode(val);
                head2->next = newNode;
                head2 = head2->next;
                l1 = l1->next;
            }
        }
        if(l2!=NULL){
            while(l2!=NULL){
                sum = l2->val + carry;
                if(sum >= 10){
                    val = sum - 10;
                    carry = 1; 
                }else{
                    val = sum;
                    carry = 0;
                }
                ListNode *newNode = new ListNode(val);
                head2->next = newNode;
                head2 = head2->next;
                l2 = l2->next;
            }
        }
        if(carry==1){
            ListNode *newNode = new ListNode(carry);
            head2->next = newNode;
        }
        return ans->next;
    }
};
