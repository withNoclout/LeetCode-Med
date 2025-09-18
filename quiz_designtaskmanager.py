import heapq

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        # tasks: [userId, taskId, priority]
        self.task_map = {}  # taskId -> [userId, priority, valid]
        self.heap = []
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = [userId, priority, True]
            heapq.heappush(self.heap, (-priority, taskId, userId))

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.task_map[taskId] = [userId, priority, True]
        heapq.heappush(self.heap, (-priority, taskId, userId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        if taskId in self.task_map and self.task_map[taskId][2]:
            userId = self.task_map[taskId][0]
            self.task_map[taskId][2] = False  # Invalidate old entry
            self.task_map[taskId] = [userId, newPriority, True]
            heapq.heappush(self.heap, (-newPriority, taskId, userId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        if taskId in self.task_map and self.task_map[taskId][2]:
            self.task_map[taskId][2] = False  # Invalidate

    def execTop(self):
        """
        :rtype: int
        """
        while self.heap:
            priority, taskId, userId = heapq.heappop(self.heap)
            if taskId in self.task_map and self.task_map[taskId][2]:
                self.task_map[taskId][2] = False
                return taskId
        return -1
