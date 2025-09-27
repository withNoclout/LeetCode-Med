class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        # restaurants[i] = [id, rating, veganFriendly, price, distance]
        filtered = []
        for r in restaurants:
            rid, rating, vegan, price, dist = r
            if veganFriendly and not vegan:
                continue
            if price > maxPrice or dist > maxDistance:
                continue
            filtered.append(r)

        # Sort: highest rating first, then highest id
        filtered.sort(key=lambda x: (-x[1], -x[0]))
        return [r[0] for r in filtered]
