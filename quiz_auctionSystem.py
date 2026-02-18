import heapq
from collections import defaultdict

class AuctionSystem(object):

    def __init__(self):
        # Dictionary to store the current valid bid for each user on each item.
        # Structure: bids[itemId][userId] = currentBidAmount
        self.bids = defaultdict(dict)
        
        # Dictionary to store a min-heap for each item to track highest bids.
        # We store (-amount, -userId) to simulate a max-heap where highest amount
        # and highest userId (for ties) come first.
        self.heaps = defaultdict(list)

    def addBid(self, userId, itemId, bidAmount):
        """
        :type userId: int
        :type itemId: int
        :type bidAmount: int
        :rtype: None
        """
        # Update the source of truth
        self.bids[itemId][userId] = bidAmount
        
        # Push to heap. If a previous bid existed, it remains in the heap 
        # but becomes "stale" (handled in getHighestBidder).
        heapq.heappush(self.heaps[itemId], (-bidAmount, -userId))

    def updateBid(self, userId, itemId, newAmount):
        """
        :type userId: int
        :type itemId: int
        :type newAmount: int
        :rtype: None
        """
        # Identical logic to addBid: update truth, push new version to heap
        self.bids[itemId][userId] = newAmount
        heapq.heappush(self.heaps[itemId], (-newAmount, -userId))

    def removeBid(self, userId, itemId):
        """
        :type userId: int
        :type itemId: int
        :rtype: None
        """
        # Remove from the source of truth
        if itemId in self.bids and userId in self.bids[itemId]:
            del self.bids[itemId][userId]
        
        # We do NOT remove from heap here to avoid O(N) scan.
        # The entry in the heap is now stale because it won't be found in self.bids.

    def getHighestBidder(self, itemId):
        """
        :type itemId: int
        :rtype: int
        """
        if itemId not in self.heaps:
            return -1
        
        heap = self.heaps[itemId]
        
        while heap:
            # Peek at the top of the heap
            neg_amount, neg_user_id = heap[0]
            
            amount = -neg_amount
            userId = -neg_user_id
            
            # Check if this heap entry is still valid
            current_item_bids = self.bids.get(itemId, {})
            
            # A bid is valid if the user still has a bid on this item 
            # AND the amount matches the current recorded amount.
            if userId in current_item_bids and current_item_bids[userId] == amount:
                return userId
            else:
                # This is a stale entry (either removed or updated), discard it
                heapq.heappop(heap)
                
        return -1

# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
