class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> m;
        for(auto& str:strs){
            string sorted_str = str;
            sort(sorted_str.begin(), sorted_str.end());
            m[sorted_str].push_back(str);
        }
        vector<vector<string>> res;
        for(auto& key:m){
            res.push_back(key.second);
        }
        return res;
    }
};
