class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        missing_type = 3
        if any(c.islower() for c in password): missing_type -= 1
        if any(c.isupper() for c in password): missing_type -= 1
        if any(c.isdigit() for c in password): missing_type -= 1
        
        n = len(password)
        
        if n < 6:
            return max(missing_type, 6 - n)
        
        repeats = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                repeats.append(length)
            i = j
            
        if n <= 20:
            replacements = sum(l // 3 for l in repeats)
            return max(missing_type, replacements)
            
        delete_count = n - 20
        left_over_deletes = delete_count
        
        for i in range(len(repeats)):
            if repeats[i] % 3 == 0 and left_over_deletes >= 1:
                repeats[i] -= 1
                left_over_deletes -= 1
                
        for i in range(len(repeats)):
            if repeats[i] % 3 == 1 and left_over_deletes >= 2:
                repeats[i] -= 2
                left_over_deletes -= 2
                
        for i in range(len(repeats)):
            if left_over_deletes > 0 and repeats[i] >= 3:
                dels = min(repeats[i] - 2, left_over_deletes)
                repeats[i] -= dels
                left_over_deletes -= dels
                
        replacements = sum(l // 3 for l in repeats)
        
        return delete_count + max(missing_type, replacements)
