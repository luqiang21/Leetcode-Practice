/*
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [m, n], which means the matrix is m * n.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

 

Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
*/

/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int x, int y);
 *     vector<int> dimensions();
 * };
 */

class Solution {
public:
    int leftMostColumnWithOneBinary(BinaryMatrix &binaryMatrix) {
        vector<int> dim = binaryMatrix.dimensions();
        int res = -1;
        for (int r = 0; r < dim[0]; ++r) {
            int temp = findFirstOne(binaryMatrix, r, dim[1]);
            if (res == -1 && temp != -1) {
                res = temp;
            }
            else if (res != -1 && temp != -1) {
                res = min(res, temp);
            }
        }
        
        return res;
    }
    
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        vector<int> dim = binaryMatrix.dimensions();
        int r = 0, c = dim[1]-1;
        while (r < dim[0] && c >= 0) {
            while (c >= 0 && binaryMatrix.get(r, c) == 1) c--;
            r++;
        }
        
        return (c == dim[1] - 1) ? -1 : c+1;
    }
private:
    int findFirstOne(BinaryMatrix &binaryMatrix, int row, int cols) {
        int left = 0, right = cols;
        while (left < right) {
            int mid = left + (right - left) / 2;
            int val = binaryMatrix.get(row, mid);
            if (val == 1) right = mid;
            else left = mid + 1;
        }
        
        return right == cols ? -1 : right;
    }
};
