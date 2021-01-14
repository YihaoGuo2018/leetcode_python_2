class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        def max_points_on_a_line_containing_point_i(i):

            def add_line(i, j, count, duplicates):

                x1 = points[i].x
                y1 = points[i].y
                x2 = points[j].x
                y2 = points[j].y
                # add a duplicate point
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                # add a horisontal line : y = const
                elif y1 == y2:
                    nonlocal horisontal_lines
                    horisontal_lines += 1
                    count = max(horisontal_lines, count)
                # add a line : x = slope * y + c
                # only slope is needed for a hash-map
                # since we always start from the same point
                else:
                    slope = (x1 - x2) / (y1 - y2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)
                return count, duplicates

            # init lines passing through point i
            lines, horisontal_lines = {}, 1
            # One starts with just one point on a line : point i.
            count = 1
            # There is no duplicates of a point i so far.
            duplicates = 0
            # Compute lines passing through point i (fixed)
            # and point j (interation).
            # Update in a loop the number of points on a line
            # and the number of duplicates of point i.
            for j in range(i + 1, n):
                count, duplicates = add_line(i, j, count, duplicates)
            return count + duplicates

        # If the number of points is less than 3
        # they are all on the same line.
        n = len(points)
        if n < 3:
            return n

        max_count = 1
        # Compute in a loop a max number of points
        # on a line containing point i.
        for i in range(n - 1):
            max_count = max(max_points_on_a_line_containing_point_i(i), max_count)
        return max_count