class Solution:
    def checkStraighLine(self, coordinates):
        diff_y = coordinates[1][1] - coordinates[0][1]
        diff_x = coordinates[1][0] - coordinates[0][0]
        if diff_y != 0:
            slope = diff_y / diff_x
            intercept = coordinates[0][1] - slope * coordinates[0][0]
            arr = list(map(lambda x: slope * x[0] + intercept - x[1], coordinates))
            return sum(arr) == 0
        else: 
            y = coordinates[0][1]
            arr = list(map(lambda x: x[1] != y, coordinates))
            return sum(arr) == 0
    
# mathematical solution
# time complexity o(N)
# space complexity o(N)


    # anther solution:
    def checkStringLine(self, coordinates):
        (x0, x0), (x1, y1) = coordiantes[:2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)
