class Solution:
    def numOfUnplacedFruits(self, fruits , baskets ) : 
        rem = 0
        n = len(baskets)

        for fruit in fruits:
            var = 1

            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    var = 0
                    break

            rem += var

        return rem
