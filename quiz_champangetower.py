class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        # Create a 2D table to store the amount of champagne in each glass.
        # We need size up to 102 to handle the overflow from row 99 to 100 safely.
        # constraints: query_row <= 99.
        tower = [[0.0] * 102 for _ in range(102)]
        
        # Pour the initial amount into the top glass
        tower[0][0] = float(poured)
        
        # Iterate through each row to distribute the champagne
        # We only need to process up to query_row - 1 to fill query_row.
        for r in range(query_row):
            for c in range(r + 1):
                # If this glass has overflowed
                if tower[r][c] > 1:
                    excess = (tower[r][c] - 1.0) / 2.0
                    # Distribute excess to the two glasses below
                    tower[r+1][c] += excess
                    tower[r+1][c+1] += excess
                    
        # The glass can only hold 1 cup max, but our simulation might 
        # have accumulated more in the variable. Return the min.
        return min(1.0, tower[query_row][query_glass])
