class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        scores = []
        
        for r, i in zip(report, student_id):
            score = 0
            for w in r.split():
                if w in pos:
                    score += 3
                elif w in neg:
                    score -= 1
            scores.append((-score, i))
            
        scores.sort()
        return [i for _, i in scores[:k]]
