class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n =len(fruits ) 
        used = set(baskets ) 
        unplaced = 0 

        for fruit in fruits : 
            placed = False 
            for i in range( n) :
                if not  used[i] and baskets[i] >= fruit : 
                    used[i] = True 
                    placed = True 
                    break 
            if not placed : 
                unplaced += 1

        return unplaced
