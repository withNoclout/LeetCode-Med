class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        processorTime.sort()
        tasks.sort(reverse=True)
        
        res = 0
        for i, time in enumerate(processorTime):
            # Assign the next 4 largest tasks to the current smallest processor.
            # The time is determined by the largest task in this group (index i * 4).
            res = max(res, time + tasks[i * 4])
            
        return res
