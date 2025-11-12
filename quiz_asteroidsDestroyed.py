class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        cur = mass
        for a in asteroids:
            if cur < a:
                return False
            cur += a
        return True
