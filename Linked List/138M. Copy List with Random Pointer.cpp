/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

/* Method: Hash Table
           Note: we use an unordered_map. The key is the node from the original list and 
                 the value is the created new node. 
*/
class Solution {
public:
    unordered_map<Node*, Node*> m;
    Node* createNode(Node* node){
        if(node==NULL){
            return node;
        }else if(m.find(node)==m.end()){
            Node* newNode = new Node(node->val);
            newNode->next = nullptr;
            newNode->random = nullptr;
            m[node] = newNode;
            return newNode;
        }else{
            return m[node];
        }
    }
    Node* copyRandomList(Node* head) {
        Node *head2 = createNode(head);
        Node *cur2 = head2;
        Node *cur = head;
        while(cur!=NULL){
            cur2->next = createNode(cur->next);
            cur2->random = createNode(cur->random);
            cur2 = cur2->next;
            cur = cur->next;
        }
        return head2;
    }
};
