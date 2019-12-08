#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int origColor = image[sr][sc];
        fill(image, sr, sc, origColor, newColor);
        return image;
    }
    
private:
    void fill(vector<vector<int>>& image, int i, int j, int origColor, int newColor) {
        if (!isValid(image, i, j)) return;
        if (origColor != image[i][j]) return;
        
        image[i][j] = -1;
        fill(image, i - 1, j, origColor, newColor);
        fill(image, i + 1, j, origColor, newColor);
        fill(image, i, j - 1, origColor, newColor);
        fill(image, i, j + 1, origColor, newColor);
        
        image[i][j] = newColor;
    }
    
    bool isValid(vector<vector<int>>& image, int i, int j) {
        return i >= 0 && i < image.size() && j >= 0 && j < image[0].size();
    }
};

int main() {
	vector<vector<int>> image = {{1, 1, 1},
								 {1, 1, 0},
								 {1, 0, 1}};
	int sr = 1, sc = 1, newColor = 2;
	vector<vector<int>> output = {{2, 2, 2},
								  {2, 2, 0},
								  {2, 0, 1}};
	assert(Solution().floodFill(image, sr, sc, newColor) == output);
	cout << "tests passed!" << endl;	
	return 0;
}
