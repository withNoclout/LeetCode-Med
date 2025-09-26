class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = []
        prev = ""
        for f in folder:
            # check if current folder is subfolder of prev
            if not prev or not f.startswith(prev + "/"):
                res.append(f)
                prev = f
        return res
