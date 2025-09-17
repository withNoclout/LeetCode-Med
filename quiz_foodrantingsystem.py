import heapq

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []
            # Use negative rating for max-heap, and food name for tie-breaking
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.cuisine_to_heap[cuisine]
        while True:
            rating, food = heap[0]
            # Check if the top of the heap is up-to-date
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
