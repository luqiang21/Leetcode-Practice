/*
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
*/
class Solution {
public:
    bool isValidSudoku1(vector<vector<char>>& board) {

        // validate every row
        for(size_t i = 0; i < board.size(); ++i) {
            set<char> used_chars;
            for(size_t j = 0; j < board[0].size(); ++j) {
                if(board[i][j] != '.') {
                    if(!isdigit(board[i][j]) || used_chars.find(board[i][j]) != used_chars.end()) {
                        return false;
                    }

                    used_chars.insert(board[i][j]);
                }
            }
            used_chars.clear();
        }

        // validate every column
        for(size_t j = 0; j < board[0].size(); ++j) {
            set<char> used_chars;
            for(size_t i = 0; i < board.size(); ++i) {
                if(board[i][j] != '.') {
                    if(!isdigit(board[i][j]) || used_chars.find(board[i][j]) != used_chars.end()) {
                        return false;
                    }

                    used_chars.insert(board[i][j]);
                }
            }
            used_chars.clear();
        }

        // validate every sub_box
        for(size_t i = 0; i < board.size(); i += 3) {

            for(size_t j = 0; j < board[0].size(); j += 3) {
                set<char> used_chars;
                for(size_t k = 0; k < 9; ++k){
                     if(board[i + (int)k/3][j + k%3] != '.') {
                            if(!isdigit(board[i + (int)k/3][j + k%3]) || used_chars.find(board[i + (int)k/3][j + k%3]) != used_chars.end()) {
                                return false;
                            }

                            used_chars.insert(board[i + (int)k/3][j + k%3]);
                            }


                }


                used_chars.clear();
            }

        }

        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<string> row, col, subbox;
        for(size_t j = 0; j < board[0].size(); ++j) {
            for(size_t i = 0; i < board.size(); ++i) {
                char c = board[i][j];
                if(c == '.') continue;
                if(!row.insert(string(1, c) + string(" in row ") + to_string(i)).second
                  || !col.insert(string(1, c) + string(" in col ") + to_string(j)).second
                  || !subbox.insert((string(1, c) + string(" in box [") + to_string(i/3) + "][" + to_string(j/3) + "]")).second                     ) return false;
            }
        }
        return true;

    }

};
