class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        # Step 2: insert person at index = k
        for p in people:
            queue.insert(p[1], p)
        
        return queue
