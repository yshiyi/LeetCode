"""
给定一些list 代表 [[start_pos，end_pos， speed]] 然后再给一个给定的pos 求当时的速度
后覆盖的为最新的
[11, 20, 5]
[10, 13, 3]
n = 11
则返回3

We want to write a class that provides us a way to add and
query for speed limits along a straight road.
Positions in the road are addressed by just a floating point value representing
distance from some arbitrarily denoted location. This distance can be negative.

Speed limits can be added by specifying an interval
in which it is active and the speed limit itself.

speed_limits.add_limit(start, end, speed_limit)

And to query for speed limits that have been added,
we simply need to provide a position

speed_limits.query(6)

where x is the distance along the road we want the speed limit for.

The user can make multiple additions of the speed limit, for example
speed_limits.add_limit(5, 100, 25). 5, 10000, 25. 6, 7. 7, 8 9, 100 11, 15, 10, ,16 30 25. 30 40 10. 40 100 25
speed_limits.add_limit(10, 15, 10)
speed_limits.add_limit(30, 40, 10)

If the user adds speed limits with overlapping intervals, we want to return
the lower limit. The time complexity for query function has to be less than O(n)

class SpeedLimits(object):
    def __init__(self):
        

    def add_limit(self, start, end, speed_limit):
        
        

    def query(self, x):
"""
