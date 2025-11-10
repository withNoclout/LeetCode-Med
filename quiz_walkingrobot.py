class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.w = width
        self.h = height
        # perimeter length in steps around the border
        self.per = 2 * (width + height) - 4
        self.idx = 0          # distance along the border starting from (0,0) going East
        self.moved = False    # whether we've taken at least one step

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        if self.per == 0:
            return
        num %= self.per
        if num:
            self.idx = (self.idx + num) % self.per
            self.moved = True

    def getPos(self):
        """
        :rtype: List[int]
        """
        i = self.idx
        w, h = self.w, self.h

        # Segment 1: bottom edge (0,0) -> (w-1,0), length w-1
        if i < w - 1:
            return [i, 0]
        i -= (w - 1)

        # Segment 2: right edge (w-1,0) -> (w-1,h-1), length h-1
        if i < h - 1:
            return [w - 1, i]
        i -= (h - 1)

        # Segment 3: top edge (w-1,h-1) -> (0,h-1), length w-1
        if i < w - 1:
            return [w - 1 - i, h - 1]
        i -= (w - 1)

        # Segment 4: left edge (0,h-1) -> (0,0), length h-1
        return [0, h - 1 - i]

    def getDir(self):
        """
        :rtype: str
        """
        # Special rule: after at least one full lap, standing at (0,0) faces "South"
        if self.idx == 0:
            return "South" if self.moved else "East"

        i = self.idx
        w, h = self.w, self.h

        if i < w - 1:
            return "East"
        i -= (w - 1)

        if i < h - 1:
            return "North"
        i -= (h - 1)

        if i < w - 1:
            return "West"
        # i -= (w - 1)

        return "South"
