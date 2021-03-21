/* Method 1: Standard way.
             Using rand() % n to return a random value between 0 to n.
             The return the value at this position in the set.
             But the time complexity of the worst case is O(N).
*/
class RandomizedSet {
public:
    set<int> s;
    /** Initialize your data structure here. */
    RandomizedSet() {
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(s.find(val)==s.end()){
            s.insert(val);
            return true;
        }else{
            return false;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(s.find(val)!=s.end()){
            s.erase(val);
            return true;
        }else{
            return false;
        }
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int n = s.size();
        int r = rand() % n;
        set<int>::iterator it = s.begin();
        int i = 0;
        while(i<r){
            it++;
            i++;
        }
        return *it;
    }
};


/* Method 2: Create a vector to hold the values.
             Choose a value from a vector is O(1).
*/
class RandomizedSet {
public:
    map<int, int> m;
    vector<int> vec;
    /** Initialize your data structure here. */
    RandomizedSet() {
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(m.find(val)==m.end()){
            int n = m.size();
            m[val] = n;
            vec.push_back(val);
            return true;
        }else{
            return false;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(m.find(val)!=m.end()){
            int v = vec[m.size()-1];
            int v_index = m[v];
            if(v!=val){
                swap(vec[m.size()-1], vec[m[val]]);
                m[v] = m[val];
            }
            vec.pop_back();
            m.erase(val);
            return true;
        }else{
            return false;
        }
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int n = m.size();
        int r = rand() % n;
        return vec[r];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
