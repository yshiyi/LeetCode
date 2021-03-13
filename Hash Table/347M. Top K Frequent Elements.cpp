class Solution {
public:
    
    /* myCompare is declared as a member function of class Solution, 
       and hence requires this pointer for calling it. 
       The complete tag for functions like bool cmp is:
       bool myCompare(Solution* this, pair<int, int>& p1, pair<int, int>& p2)
       We can declare it as a static funtion, since static functions do not require this pointer for calling.
    
    */
    static bool myCompare(pair<int, int>& p1, pair<int, int>& p2) {
        return p1.second > p2.second;
    }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        /* Method 1: First, use a map to count the appearances of each unique element,
                     Then, use a multimap to flip the key and value in map.
                     Finally, save the last k elements to a vector.
        */
        map<int, int> m;
        for (auto& val:nums) {
            if (m.find(val) != m.end()) {
                m[val]++;
            }else {
                m.insert(make_pair(val, 1));
            }
        }
        
        multimap<int, int> mm;
        for (auto& key:m) {
            mm.insert(make_pair(key.second, key.first));
        }
        
        vector<int> res;
        multimap<int, int>::reverse_iterator it = mm.rbegin();
        for (int i=0; i<k; ++i) {
            res.push_back(it->second);
            it++;
        }
        
        return res;
        
        
        /* Method 2: First, create a map. 
                     The kay is the unique elements, the value is the currect size of vecValues.
                     Create a vector of pairs of integers. The index of the vector is the value of the map.
                     The first value of the pair is the unique element, 
                     and the second value of the pair is the number of appearances.
                     Then sort this vector using self-defined functional object (it must be static).
                     Finally, save the first k elements to vecAnswer.
        */
        unordered_map<int, int> mapValues;
        vector<pair<int, int>> vecValues;
        vector<int> vecAnswer;
        
        for(auto& val:nums)
        {
            if(mapValues.find(val) != mapValues.end())
            {
                vecValues[mapValues[val]].second++;
            }
            else
            {
                mapValues[val] = vecValues.size();
                vecValues.emplace_back(pair<int,int>{val, 1});
            }
        }
        
        sort(vecValues.begin(), vecValues.end(), myCompare);
        for(int nIndex = 0; nIndex < k; nIndex++)
        {
            vecAnswer.push_back(vecValues[nIndex].first);
        }
        return vecAnswer;
        
        
    }
};




/* Method 3: Using inheritance and predicate to sort the vector.

*/
class myCompare {
public:
    bool operator()(pair<int, int>& p1, pair<int, int>& p2) {
        return p1.second > p2.second;
    }
};

class Solution : public myCompare {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mapValues;
        vector<pair<int, int>> vecValues;
        vector<int> vecAnswer;
        
        for(auto& val:nums)
        {
            if(mapValues.find(val) != mapValues.end())
            {
                vecValues[mapValues[val]].second++;
            }
            else
            {
                mapValues[val] = vecValues.size();
                vecValues.emplace_back(pair<int,int>{val, 1});
            }
        }
        
        sort(vecValues.begin(), vecValues.end(), myCompare());
        for(int nIndex = 0; nIndex < k; nIndex++)
        {
            vecAnswer.push_back(vecValues[nIndex].first);
        }
        return vecAnswer;
        
        
    }
};
