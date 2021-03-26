/*
  Singly Linked List
*/
class MyLinkedList {
private:
    struct node {
        int val;
        node *next;
    };
    node *head;
    int size;
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        head = nullptr;
        size = 0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if(index<0 || index >=size){
            return -1;
        }
        node *cur = new node;
        cur = head;
        
        for(int i=0; i<index; i++){
            cur = cur->next;
        }
        return cur->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if(index<0 || index>size){
            return;
        }
        node *cur = new node;
        cur = head;
        node *newNode = new node;
        newNode->val = val;
        if(index==0){
            newNode->next = cur;
            head = newNode;
        }else{
            for(int i=0; i<index-1; i++){
                cur = cur->next;
            }
            newNode->next = cur->next;
            cur->next = newNode;
        }
        size++;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if(index<0 || index>=size){
            return;
        }
        node *cur = new node;
        cur = head;
        
        if(index==0){
            head = cur->next;
        }else{
            for(int i=0; i<index-1; i++){
                cur = cur->next;
            }
            cur->next = cur->next->next;
        }
        size--;
    }
};

/*
  Doubly Linked List
  Note: as there is a previous pointer in doubly linked lists, we need to make sure ->next is not nullptr every 
        time when we get there.
*/
class MyLinkedList {
private:
    struct node {
        int val;
        node *next;
        node *previous;
    };
    node *head;
    int size;
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        head = nullptr;
        size = 0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if(index<0 || index >=size){
            return -1;
        }
        node *cur = new node;
        cur = head;
        
        for(int i=0; i<index; i++){
            cur = cur->next;
        }
        return cur->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if(index<0 || index>size){
            return;
        }
        node *cur = new node;
        cur = head;
        node *newNode = new node;
        newNode->val = val;
        newNode->previous = nullptr;
        if(index==0){
            newNode->next = cur;
            if(head!=nullptr){
                cur->previous = newNode;
            }
            head = newNode;
        }else{
            for(int i=0; i<index-1; i++){
                cur = cur->next;
            }
            node *temp = cur->next;
            if(temp!=nullptr){
                temp->previous = newNode;
            }
            newNode->next = temp;
            cur->next = newNode;
            newNode->previous = cur;
        }
        size++;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if(index<0 || index>=size){
            return;
        }
        node *cur = new node;
        cur = head;
        
        if(index==0){
            head = cur->next;
            if(head!=nullptr){
                head->previous = nullptr;
            }
        }else{
            for(int i=0; i<index; i++){
                cur = cur->next;
            }
            node *temp1 = cur->previous;
            node *temp2 = cur->next;
            temp1->next = cur->next;
            if(temp2!=nullptr){
                temp2->previous = cur->previous;
            }
        }
        size--;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
