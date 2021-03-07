class MyHashSet {
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        
    }
    
    void add(int key) {
        s.insert(key);
    }
    
    void remove(int key) {
        it = s.find(key);
        if (this->contains(key)) {
            s.erase(key);
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        it = s.find(key);
        if(it != s.end()) {
            return true;
        }else {
            return false;
        }
    }
private:
    set<int> s;
    set<int>::iterator it;
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
