/*
146M. LRU Cache

Description:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
2. int get(int key) Return the value of the key if the key exists, otherwise return -1.
3. void put(int key, int value) Update the value of the key if the key exists. 
   Otherwise, add the key-value pair to the cache. 
   If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
 

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
*/

/*
Time complexity: O(1)
Space complexity: O(n), n is the size of capacity
*/
class LRUCache {
private:
    // Declare the size
    int cap;
    // This is a list of pair of two integers, which are key and value.
    list<pair<int, int>> l;
    // The key in the map is the key value, the value saved in the key is 
    // an iterator/a pointer which points to the position of the key in the list.
    // e.g. list = [1, 2] -> [3, 4] -> [5, 6]
    //      map = {{1, list.begin()}, {3, list.begin()+1}, {5, list.begin()+2}}
    map<int, list<pair<int, int>>::iterator> m;
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        // If the key is not in the map, return -1.
        if(m.count(key)==0){
            return -1;
        }
        // it is the iterator/pointer saved in m[key].
        auto it = m[key];
        // We use list.splic(newPos, targetValue, targetValue_startPos, targetValue_endPos)
        // to move the key to the front of the list
        l.splice(l.begin(), l, it);
        // it is an iterator of the list, it->first is the key and it->second is the value.
        return it->second;
        
    }
    
    void put(int key, int value) {
        // If the key already exists, remove it first.
        if(m.count(key)){
            l.erase(m[key]);
        }
        // We put the new key in the front of the list.
        l.push_front(make_pair(key, value));
        // The pointer points to the new key is l.begin().
        m[key] = l.begin();
      
        // If exceeds the maximum cap, remove the last node in the list.
        if(m.size() > cap){
            // Note: b is not a pointer, b represents the pair of values saved in the last node.
            auto b = l.back();
            l.pop_back();
            m.erase(b.first);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
