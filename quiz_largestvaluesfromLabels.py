class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        pairs = sorted(zip(values, labels), reverse=True)
        label_count = {}
        res = 0
        count = 0
        for value, label in pairs:
            if label_count.get(label, 0) < useLimit:
                res += value
                label_count[label] = label_count.get(label, 0) + 1
                count += 1
                if count ==
