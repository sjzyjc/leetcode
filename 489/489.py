# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

DIRS = [[0, 1],[-1, 0], [0, -1], [1, 0]]
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, set())
        
    def dfs(self, robot, i, j, direct, cleaned):  
        robot.clean()
        cleaned.add((i, j))
        
        for offset in range(1, 5):
            robot.turnLeft()
            new_dir = (direct + offset) % 4
            
            new_i = i + DIRS[new_dir][0]
            new_j = j + DIRS[new_dir][1]
            if (new_i, new_j) not in cleaned and robot.move():
                self.dfs(robot, new_i, new_j, new_dir, cleaned)
                  
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
                