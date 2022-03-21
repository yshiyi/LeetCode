/*
631H. Design Excel Sum Formula
Description:
Your task is to design the basic function of Excel and implement the function of sum formula. 
Specifically, you need to implement the following functions:
Excel(int H, char W): This is the constructor. The inputs represents the height and width of the Excel form. 
H is a positive integer, range from 1 to 26. It represents the height. 
W is a character range from 'A' to 'Z'. It represents that the width is the number of characters from 'A' to W. 
The Excel form content is represented by a height * width 2D integer array C, it should be initialized to zero. 
You should assume that the first row of C starts from 1, and the first column of C starts from 'A'.
void Set(int row, char column, int val): Change the value at C(row, column) to be val.
int Get(int row, char column): Return the value at C(row, column).
int Sum(int row, char column, List of Strings : numbers): This function calculate and set the value at C(row, column),
where the value should be the sum of cells represented by numbers. 
This function return the sum result at C(row, column). 
This sum formula should exist until this cell is overlapped by another value or another sum formula.
numbers is a list of strings that each string represent a cell or a range of cells. 
If the string represent a single cell, then it has the following format : ColRow. 
For example, "F7" represents the cell at (7, F).
If the string represent a range of cells, then it has the following format : ColRow1:ColRow2. 
The range will always be a rectangle, and ColRow1 represent the position of the top-left cell, 
and ColRow2 represents the position of the bottom-right cell.
Example 1:
Excel(3,"C"); 
// construct a 3*3 2D array with all zero.
//   A B C
// 1 0 0 0
// 2 0 0 0
// 3 0 0 0
Set(1, "A", 2);
// set C(1,"A") to be 2.
//   A B C
// 1 2 0 0
// 2 0 0 0
// 3 0 0 0
Sum(3, "C", ["A1", "A1:B2"]);
// set C(3,"C") to be the sum of value at C(1,"A") and the values sum of the rectangle range 
whose top-left cell is C(1,"A") and bottom-right cell is C(2,"B"). Return 4. 
//   A B C
// 1 2 0 0
// 2 0 0 0
// 3 0 0 4
Set(2, "B", 2);
// set C(2,"B") to be 2. Note C(3, "C") should also be changed.
//   A B C
// 1 2 0 0
// 2 0 2 0
// 3 0 0 6
Note:
You could assume that there won't be any circular sum reference. For example, A1 = sum(B1) and B1 = sum(A1).
The test cases are using double-quotes to represent a character.
Please remember to RESET your class variables declared in class Excel, 
as static/class variables are persisted across multiple test cases. Please see here for more details.
*/

/*
Method: Topological Sort
        We need to create and maintain two types of relations between cells.
        For example, C3 = A1 + A1 + B1 + A2 + B2. (input is "A1", "A1:B2")
        The first relation is from the parent to child, as well as the number of child's appearance
        forward[A1] = {[C3], 2}, forward[B1] = {[C3], 1},, forward[A2] = {[C3], 1},, forward[B2] = {[C3], 1}.
        The second relation is from the child to parent (record all the parent cells)
        backward[C3] = {A1, A2, B1, B2}.
*/
#include <iostream>
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <queue>
using namespace std;

class Excel {
private:
    // This is a 2D array which is used to contain all the values.
    vector<vector<int>> Exl;
    // Maintain the relation from parent to child
    // For simplicity, the position of each cell is encoded as an integer (row*26+col)
    unordered_map<int, unordered_map<int, int>> fward;
    // Maintain the relation from child to parent
    unordered_map<int, unordered_set<int>> bward;
public:
    Excel(int H, char W){
        // Initialize the form
        // Note: to easily set and get value from the cell, we create H+1 rows instead of H.
        // e.g., for input 1, 'C'. If we create 1 row, then later Exl[1][col] is not accessable.
        Exl = vector<vector<int>> (H+1, vector<int>(W-'A'+1, 0));
        fward.clear();
        bward.clear();
    }

    void set(int r, char c, int v){
        // key is the encoded position of the cell
        int col = c-'A', key = r*26+col;
        // Update the cell value
        // If this cell is the parent of any other cell, we also need to update the values of its children cells.
        update(r, col, v);
        // If this cell is the child of any other cells, we have to break the relation.
        if(bward.count(key)){
            for(auto ele:bward[key]){
                fward[ele].erase(key);
            }
            bward[key].clear();
        }
    }
    
    // This function is created to update the values in all the children cells of the target cell.
    void update(int r, int c, int v){
        int prev = Exl[r][c];
        Exl[r][c] = v;
        // Here, we apply bfs method.
        // q is created to hold all the children cells. 
        // update is to record the difference between the new and previous value.
        queue<int> q, update;
        q.push(r*26+c);
        update.push(v-prev);
        while(!q.empty()){
            int key = q.front(), diff = update.front();
            q.pop(); update.pop();
            if(fward.count(key)){
                for(auto ele:fward[key]){
                    q.push(ele.first);
                    update.push(ele.second*diff);
                    Exl[ele.first/26][ele.first%26] += diff*ele.second;
                }
            }
        }
    }

    int get(int r, char c){
        return Exl[r][c-'A'];
    }

    int sum(int r, char c, vector<string> strs){
        int col = c - 'A', key = r*26+col, ans = 0;
        // We must check if this cell is a child of any other cells.
        // If it is, then we must break all the relation.
        if(bward.count(key)){
            for(auto ele:bward[key]){
                fward[ele].erase(key);
            }
            bward[key].clear();
        }

        for(auto str:strs){
            // We need to determine the range. For example, "A11:B21"
            // left = A, right = B, top = 11, bottom = 21
            int p = str.find(':'), left, right, top, bottom;
            left = str[0] - 'A';
            if(p == -1){
                top = stoi(str.substr(1));
                right = left;
            }else{
                top = stoi(str.substr(1, p-1));
                right = str[p+1] - 'A';
            }
            bottom = stoi(str.substr(p+2));

            for(int i=top; i<=bottom; ++i){
                for(int j=left; j<=right; ++j){
                    ans += Exl[i][j];
                    ++fward[i*26+j][key];
                    bward[key].insert(i*26+j);
                }
            }
        }
        
        // Notice, every time when we create a relation, we must update all its children cells as well.
        update(r, col, ans);
        return ans;
    }

};

int main(){
    Excel *obj = new Excel(3, 'C');
    obj->set(1, 'A', 2);
    obj->sum(3, 'C', {"A1", "A1:B2"});
    cout << obj->get(3, 'C') << endl;
    obj->set(2, 'B', 2);
    cout << obj->get(3, 'C') << endl;

}
