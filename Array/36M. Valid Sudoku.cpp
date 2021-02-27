class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        // Create 3 vectors of sets and each vector contains 9 sets.
        vector<set<int>> v_row, v_col, v_box;
        v_row.resize(9);
        v_col.resize(9);
        v_box.resize(9);
        
        for (int i=0; i<board.size(); i++) {
            for (int j=0; j<board[i].size(); j++) {
                if (board[i][j] != '.') {
                    
                    /* For char variable, 
                       1. char - '0' can convert '0' -> 0, '1' -> 1.
                       2. char c = 'a'; int ic = (int)c; value of ic is 97
                    */
                    int num = board[i][j]-'0';
                    int box_index = i/3 * 3 + j/3;
                    // cout << i << " " << j << " " << box_index << " " << num << endl;
                    if (v_row[i].find(num)!=v_row[i].end() || v_col[j].find(num) != v_col[j].end() || v_box[box_index].find(num) != v_box[box_index].end()) {
                        return false;
                    }else {
                        v_row[i].insert(num);
                        v_col[j].insert(num);
                        v_box[box_index].insert(num);
                    }
                }
            }
        }
        return true;
    }
};
