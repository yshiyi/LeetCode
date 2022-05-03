"""
Consider a robot and n cities (numbered 0 through n - 1) connected by m bidirectional roads. 
The robot starts at city 0, and at each step can move to another city that is directly connected to it by a road 
or choose to stay at its current city. 
Each time it visits city i, it receives r_i dollars and uses 1 unit of fuel. 
If the robot stays at a city, it does not gain additional reward but also does not spend any fuel. 
The total cost of fuel for a path using f units of fuel is f^2 dollars. 
What is the maximum number of dollars the robot can gain, such that the robot returns to city 0 at the end of its path? 
Assume r_0 = 0
"""
