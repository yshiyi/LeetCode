/*
68H. Text Justification

Description:
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters 
and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", 
because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to",
                "a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
*/

/*
Method: 1. Determine the number of words put in the same line
        2. Modify the space between the words
            a. Not the last line
            b. Last line or a very long word (this long word can be treated as the last line)
        3. stringBuilder function to build each line
        
        Variables:
        1. i: word index, track the index in string words
        2. end: this is the word index of the last word in the line
        3. l: this is the length of all words in one line / it is the total # of characters in one line
        4. n: # of space added between two words. n = (maxL - l)/(end - start)
        5. m: # of gaps in which we should add one extra space. m = (maxL - l)%(end - start)
           e.g. (17 - 7)/(4 - 0) = 2, we add 2 spaces between two words first
                (17 - 7)%(4 - 0) = 1, we add one extra space in the first and second gap
        
        For the last line or the very long word, we just simply fill in the rest of line with space.
        
        Time complexity: O(N), where N = sum(len(word)) is the total number of characters
        Space complexity: O(N)
*/
class Solution {
public:
    string stringBuilder(vector<string>& words, int start, int end, int len, int maxL, bool lastL){
        string line;
        if(lastL){
            // If this is the last line, we add word from words[start]
            // to words[end-1] with a space.
            for(int i=start; i<end; ++i){
                line += words[i] + " ";
            }
            // Add the last word
            line += words[end];
            // If the length is less than the maximum width, we fill
            // the space in the rest of line.
            while(line.size()<maxL){
                line += " ";
            }
        }else{
            // Calculate the number of extra space needed to be added
            // between two words
            int n = (maxL - len)/(end - start);
            // Calculate the number of gaps need one extra space
            int m = (maxL - len)%(end - start);
            string space(n, ' ');
            for(int i=start; i<start+m; ++i){
                line += words[i] + space + " ";
            }
            for(int i=start+m; i<end; ++i){
                line += words[i] + space;
            }
            line += words[end];
        }
        return line;
    }
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        // Define i to iterate over the words
        int i = 0;
        while(i < words.size()){
            // Define l to record the length of the current line
            int l = 0;
            // Record the start index
            int start = i;
            while(i < words.size() && l + words[i].size()<=maxWidth){
                l += words[i].size() + 1;
                ++i;
            }

            // Check if this is the last line
            // There is a special case, e.g. a very long single word
            // In this case, we treat it as the last line as we will
            // insert extra space after that word.
            bool last = ((i==words.size()) || (start == i-1));
            // l-(i-start) is the total length of words except spaces
            // i-start: number of space we added when calculating l
            res.push_back(stringBuilder(words, start, i-1, l-(i-start), maxWidth, last));
             
        }
        return res;
    }
};
