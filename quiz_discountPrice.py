class Solution(object):
    def discountPrices(self, sentence, discount):
        words = sentence.split()
        d = (100 - discount) / 100.0
        
        for i in range(len(words)):
            w = words[i]
            if len(w) > 1 and w[0] == '$' and w[1:].isdigit():
                price = int(w[1:])
                new_price = price * d
                words[i] = "$" + "{:.2f}".format(new_price)
        
        return " ".join(words)
