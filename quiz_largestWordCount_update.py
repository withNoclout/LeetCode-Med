class Solution(object):
    def largestWordCount(self, messages, senders):
        count = {}
        for msg, sender in zip(messages, senders):
            count[sender] = count.get(sender, 0) + len(msg.split())
        
        max_count = max(count.values())
        ans = ""
        for sender, c in count.items():
            if c == max_count:
                ans = max(ans, sender)
        return ans
