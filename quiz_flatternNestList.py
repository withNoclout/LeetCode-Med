# The interface for NestedInteger is provided by the judge:
# class NestedInteger:
#     def isInteger(self) -> bool: ...
#     def getInteger(self) -> int: ...
#     def getList(self) -> ['NestedInteger']: ...

class NestedIterator:
    def __init__(self, nestedList):
        self.flat = []
        self.i = 0
        self._flatten(nestedList)

    def _flatten(self, lst):
        for x in lst:
            if x.isInteger():
                self.flat.append(x.getInteger())
            else:
                self._flatten(x.getList())

    def next(self) -> int:
        val = self.flat[self.i]
        self.i += 1
        return val

    def hasNext(self) -> bool:
        return self.i < len(self.flat)
