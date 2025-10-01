class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # Clamp circle center to rectangle boundaries
        # Find closest point on rectangle to circle center
        closest_x = min(max(xCenter, x1), x2)
        closest_y = min(max(yCenter, y1), y2)

        # Distance from circle center to closest point
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        # Check if distance is within circle radius
        return dx * dx + dy * dy <= radius * radius

