class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []  # function id stack
        prev_time = 0

        for log in logs:
            fid, typ, t = log.split(":")
            fid, t = int(fid), int(t)

            if typ == "start":
                if stack:
                    # Add time spent by the function on top of stack before this new call
                    res[stack[-1]] += t - prev_time
                stack.append(fid)
                prev_time = t
            else:  # "end"
                res[stack.pop()] += t - prev_time + 1
                prev_time = t + 1

        return res
