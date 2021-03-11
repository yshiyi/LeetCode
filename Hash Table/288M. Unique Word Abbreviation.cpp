/*
288M. Unique Word Abbreviation
Hash Table, Design
Description:
An abbreviation of a word follows the form <first letter><number of characters><last letter>. Below are some examples of word abbreviations:
a) it                      --> it    (no abbreviation)
     1
b) d|o|g                   --> d1g
              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n
              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
Example:
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") -> false    "deer" and "door" have the same abbreviation
isUnique("cart") -> true     no other words have the same abbre
isUnique("cane") -> false    "cake" has the same abbre
isUnique("make") -> true     no other words have the same abbre
*/

//
// Created by Shiyi Yang on 2021-03-11.
//
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class ValidWordAbbre {
public:
    ValidWordAbbre(vector<string>& words) {
        for (int i=0; i<words.size(); ++i) {
            string abbre = convertToAbbre(words[i]);
            if (m.find(abbre) == m.end()) {
                m.insert(make_pair(abbre, 1));
            }else {
                m[abbre]++;
            }
        }
    }

    bool isUnique(string& word) {
        string abbre = convertToAbbre(word);
        if (m[abbre] == 1) {
            return true;
        }else {
            return false;
        }
    }

    string convertToAbbre(string& word) {
        string res;
        int l = word.size();
        res = word[0] + to_string(l) + word[l-1];
        return res;
    }

    void printMap() {
        for (auto& ele:m) {
            cout << ele.first << " " << ele.second << endl;
        }
    }

private:
    unordered_map<string, int> m;

};

int main() {
    // vector<string> words = {"deer", "door", "cake", "card"};
    vector<string> words = {"a", "a"};

    ValidWordAbbre* obj = new ValidWordAbbre(words);
    obj->printMap();
    for (auto& word:words) {
        cout << obj->isUnique(word) << endl;
    }
    
    return 0;
}
