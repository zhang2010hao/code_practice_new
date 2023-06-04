
def maxPoints(points):
    ab2set = {}

    n = len(points)
    for i in range(n-1):
        for j in range(i+1, n):
            if points[j][0] - points[i][0] == 0:
                a = float('inf')
                b = - points[j][0]
            else:
                a = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                b = (points[i][0] * points[j][1] - points[i][1] * points[j][0]) / (points[i][0] - points[j][0])

            pset = ab2set.get((a, b), set())
            pset.add(i)
            pset.add(j)
            ab2set[(a, b)] = pset


    return max([len(v) for v in ab2set.values()])

points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
rest = maxPoints(points)
print(rest)