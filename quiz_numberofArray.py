class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        s = 0
        min_s = 0
        max_s = 0
        for d in differences:
            s += d
            if s < min_s:
                min_s = s
            if s > max_s:
                max_s = s

        # x must satisfy: lower - min_s <= x <= upper - max_s
        left = lower - min_s
        right = upper - max_s
        return max(0, right - left + 1)
