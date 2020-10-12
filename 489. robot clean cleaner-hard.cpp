/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
public:
    // dfs and backtracking
    void cleanRoom(Robot& robot) {
        set<pair<int, int>> visited;
        // dir: 0 up, 1 right, 2 down, 3 left
        dfs(visited, 0, 0, 0, robot);
    }
    
    void dfs(set<pair<int, int>>& visited, int i, int j, int curDir, Robot& robot) {
        if (visited.count({i, j})) return;
        visited.insert({i, j});
        robot.clean();
        
        for (int k = 0; k < 4; ++k) {
            int x = i, y = j;
            if (robot.move()) {
                switch(curDir) {
                    case 0: x--; break;
                    case 1: y++; break;
                    case 2: x++; break;
                    case 3: y--; break;
                }
                dfs(visited, x, y, curDir, robot);
                
                // go back to original place
                robot.turnRight();
                robot.turnRight();
                robot.move();
                
                robot.turnRight();
                robot.turnRight();
            }
            
            robot.turnRight();
            curDir += 1;
            curDir %= 4;
        }
    }
};
