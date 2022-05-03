"""
给一个list of 3D点和一个value k，如果A跟B的euclidean distance小于k，那么它们在同一个cluster。
如果A跟C的距离大于k，但是B跟C的距离小于k，A，B，C都还是算在同一个cluster里。
现在是要output所有的cluster。

思路也参考了地里之前的解法，先建立一个graph，不同点之间如果距离小于k就加一条edge，最后output 所有的connected components。
"""
