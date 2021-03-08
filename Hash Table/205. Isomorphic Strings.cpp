class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int sl = s.size(), tl = t.size();
        if (sl != tl) {return false;}
        map<char, int> ms, mt;
        map<char, int>::iterator its, itt;
        for (int i=0; i<sl; i++) {
            its = ms.find(s[i]);
            itt = mt.find(t[i]);
            if (its!=ms.end() && itt!=mt.end()) {
                if ((its)->second == (itt)->second) {
                    continue;
                }else {
                    return false;
                }
            }else if (its==ms.end() && itt==mt.end()) {
                ms.insert(make_pair(s[i], i));
                mt.insert(make_pair(t[i], i));
            }else {
                return false;
            }

        }
        return true;
    }
};
