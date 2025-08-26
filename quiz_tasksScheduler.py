
from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = Counter(tasks)
        max_freq = max(count.values())  
        max_count = list(count.values()).count(max_freq  ) 

        part_count = max_freq - 1 

        return max( len(tasks ) , 
                   part_count * (n + 1) + max_count )
