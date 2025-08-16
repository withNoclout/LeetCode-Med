# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s :
            return NestedInteger()
        if s[0] == '[' :
            return NestedInteger(int(s))
        
        stack , num , negative  = [] , None  , False 
        current = NestedInteger()
        stack.append(current) 

        for i , ch in enumerate(s) :
            if ch == '-' : 
                negative = True 
            elif ch.isdigit() : 
                num = ( num or 0 ) * 10+ int(ch) 
            elif ch in [ ',' , ']' ] :
                if num is not None : 
                    if negative : 
                        num = -num 
                    stack[-1].add(NestedInteger(num))
                num , negative = None , False 
                if ch == ']' and len(stack) >  1 : 
                    ni = stack.pop()
                    stack[-1].add(ni ) 
            elif ch == '['  :
                ni = NestedInteger()
                stack.append(ni)

        return stack[0]
