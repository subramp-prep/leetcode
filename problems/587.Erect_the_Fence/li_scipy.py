# coding=utf-8
# Author: Jianghan LI
# Question: 587.Erect_the_Fence
# Date: 2017-05-18

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):

    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        from scipy.spatial import ConvexHull
        import numpy as np

        def isHull(point, hull, tol=1e-12):
            return any((abs(np.dot(eq[:-1], point) + eq[-1]) < tol) for eq in hull.equations)
        try:
            hull = ConvexHull([(p.x, p.y) for p in points])
            return [p for p in points if isHull((p.x, p.y), hull)]
        except AttributeError:
            hull = ConvexHull(points)
            return [p for p in points if isHull(p, hull)]
        except:
            return points


############ test case ###########
# except AttributeError for local test.
s = Solution()
print s.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]])

############ comments ############
# scipy.spatial.ConvexHull(points) returns all points that form the hull.
# It helps a lot already. However, in this question, we need to return all points on the hull.
# I write a funciton isHull to check if a point is on the hull.
# When ConvexHull throws a exception, it means the points can not form a hull.
# In this case, I return all points.
