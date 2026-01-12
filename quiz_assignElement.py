class Solution(object):
    def assignElements(self, groups, elements):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_g = max(groups)
        min_elements = {}
        for i, val in enumerate(elements):
            if val not in min_elements:
                min_elements[val] = i
                
        # Precompute the smallest index for each possible divisor
        mapping = [-1] * (max_g + 1)
        sorted_el = sorted(min_elements.keys())
        for e in sorted_el:
            if e > max_g: continue
            if mapping[e] == -1: # Only process if not already assigned a smaller index
                for multiple in range(e, max_g + 1, e):
                    if mapping[multiple] == -1:
                        mapping[multiple] = min_elements[e]
        
        return [mapping[g] for g in groups]
