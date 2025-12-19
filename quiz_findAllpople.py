class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        from collections import defaultdict, deque
        from itertools import groupby

        meetings.sort(key=lambda x: x[2])
        known = {0, firstPerson}

        for t, grp in groupby(meetings, key=lambda x: x[2]):
            graph = defaultdict(list)
            people = set()
            for x, y, _ in grp:
                graph[x].append(y)
                graph[y].append(x)
                people.update([x, y])
            
            queue = deque([p for p in people if p in known])
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in known:
                        known.add(neighbor)
                        queue.append(neighbor)
        
        return list(known)
