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
        stack<int> s1, s2, sSum;
        while(l1!=NULL){
            s1.push(l1->val);
            l1 = l1->next;
        }
        while(l2!=NULL){
            s2.push(l2->val);
            l2 = l2->next;
        }
        int carry = 0, val, sum;
        while(s1.size()>0 && s2.size()>0){
            sum = s1.top() + s2.top() + carry;
            if(sum>=10){
                val = sum - 10;
                carry = 1;
            }else{
                val = sum;
                carry = 0;
            }
            sSum.push(val);
            s1.pop(); s2.pop();
        }
        while(s1.size()>0){
            sum = s1.top() + carry;
            if(sum>=10){
                val = sum - 10;
                carry = 1;
            }else{
                val = sum;
                carry = 0;
            }
            sSum.push(val);
            s1.pop();
        }
        while(s2.size()>0){
            sum = s2.top() + carry;
            if(sum>=10){
                val = sum - 10;
                carry = 1;
            }else{
                val = sum;
                carry = 0;
            }
            sSum.push(val);
            s2.pop();
        }
        if(carry==1){
            sSum.push(carry);
        }
        ListNode *head = new ListNode(0);
        ListNode *ans = head;
        while(sSum.size() > 0){
            ListNode *newNode = new ListNode(sSum.top());
            head->next = newNode;
            head = head->next;
            sSum.pop();
        }
        return ans->next;
    }
};
