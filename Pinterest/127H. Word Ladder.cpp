/*
127H. Word Ladder

Description:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:

1. Every adjacent pair of words differs by a single letter.
2. Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
3. sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest 
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
 

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

Similar Questions:
Word Ladder II - Hard
Minimum Genetic Mutation - Medium
*/

/*
Method 1: BFS
          This is a typical problem solved by using BFS.
          For each word, we replace every single letter with 'a' - 'z'.
          If the new word is the word set, we save it to the queue.
          Notice:
          1. The new word must not be the same as the original word. e.g., hit -> hot -> hit
          2. When we find a new word and push it into the queue, we must remove it from the word set.
             It also prevents the infinity loop. e.g., hit -> hot -> hit
          
          Time complexity: O(l*n), where l is the size of word and n is the length of word list.
          Space complexity: O(n)
*/
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if(!wordSet.count(endWord)){return 0;}
        queue<string> q{{beginWord}};
        int res=0;
        while(!q.empty()){
            int size = q.size();
            while(size--){
                string word = q.front(); q.pop();
                if(word==endWord){return res+1;}
                for(int i=0; i<word.size(); ++i){
                    string newWord = word;
                    for(char ch='a'; ch<='z'; ++ch){
                        newWord[i] = ch;
                        if(wordSet.count(newWord) && newWord != word){
                            q.push(newWord);
                            wordSet.erase(word);
                        }
                    }
                }
            }
            ++res;
        }
        return 0;
    }
};
