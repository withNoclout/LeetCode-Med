from collections import defaultdict 

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_map = defaultdict(list)

        for path in paths : 
            parts  =  path.split()
            directory = parts[0] 

            for file in parts[1:] : 
                file_name, content = file.split('(')
                content = content[:-1]
                full_path = directory + '/' + file_name 
                content_map[content].append(full_path)

        return [ group for group in content_map.values() if len(group) > 1]
