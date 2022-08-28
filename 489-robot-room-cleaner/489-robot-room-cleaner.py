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

class Solution:
    def dfs(self, x, y, original_direction):
        self.robot.clean()
        
        for d in range(4):
            new_direction = (original_direction + d) % 4
            
            if new_direction is 0 and (x-1, y) not in self.visited and self.robot.move():
                self.visited.add((x-1, y))
                self.dfs(x-1, y, new_direction)
            if new_direction is 1 and (x, y-1) not in self.visited and self.robot.move():
                self.visited.add((x, y-1))
                self.dfs(x, y-1, new_direction)
            if new_direction is 2 and (x+1, y) not in self.visited and self.robot.move():
                self.visited.add((x+1, y))
                self.dfs(x+1, y, new_direction)
            if new_direction is 3 and (x, y+1) not in self.visited and self.robot.move():
                self.visited.add((x, y+1))
                self.dfs(x, y+1, new_direction)
            
            self.robot.turnRight()
        
        self.robot.turnRight()
        self.robot.turnRight()
        self.robot.move()
        self.robot.turnRight()
        self.robot.turnRight()
    
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.visited = set()
        self.robot = robot
        self.dfs(0, 0, 0)
        