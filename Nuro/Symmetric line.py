"""
Given a list of 2D point coordinates, determine if a symmetrical vertical line x=a exists and return the value of that vertical line.
E.g:

[(1, 3), (2, 5), (3, 5), (4,3)] has a symmetrical line x=2.5
[(1, 3), (2, 5), (3, 5), (4, 2)] does not have a symmetrical line however
From my understanding of the question, if there exist certain points with same y-coordinate which reflect across a line 
(e.g. in case(1), points (2, 5) and (3, 5) both had a x-coordinate difference of 0.5 from x=2.5, 
and points (1, 3) and (4, 3) both had a x-coordinate difference of 1.5 from line x=2.5), 
then the function should return the value 2.5

I could not find this question on Leetcode. Could anyone figure out the solution to this one?

Some points I could make out:

number of points with common Y-coordinate being odd or even does not matter as one of those points could be along the line x=a
I feel like the vertical line could be the average of the x-coordinates of all points, but I would like to know if there is another way to calculate the line.
The cuurent solution I have is as follows:

def is_symmetric(points: list):
	y_dict = {}
	for i in range(len(points)):
		key = points[i][1]
		if key not in y_dict.keys():
			y_dict[key] = [points[i][0]]
		else:
			y_dict[key].append(points[i][0])
		
	key_list = list(y_dict.keys())
	for i in range(len(key_list)):
		prev = sum(y_dict[key_list[i - 1]]) / len(y_dict[key_list[i - 1]])
		curr = sum(y_dict[key_list[i]]) / len(y_dict[key_list[i]])
		if prev != curr:
			return None
		
	return curr
	
points = [(1, 3), (2, 5), (2, 5), (4, 3)]
print(is_symmetric(points))
"""
