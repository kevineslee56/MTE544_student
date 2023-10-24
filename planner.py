import math 

# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1

class planner:
    def __init__(self, type_):

        self.type=type_

    def plan(self, goalPoint=[0.0, 0.0, 0.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()

    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        theta = goalPoint[2]
        return x, y, theta

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
        function = "quadratic"
        
        trajectoryQuadratic = []    # [[x,y]]
        trajectorySigma = []        # [[x,y]]
        for i in range(-10,11):
            x = i / 10
            trajectoryQuadratic.append([x, x**2])
            trajectorySigma.append([x, 1/(1+math.exp(-x*3))])

        return trajectorySigma if function == "quadratic" else trajectorySigma
