class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st= [] 
        for a in asteroids:
            if a > 0:
                st.append(a)
            else:
                while st and st[-1] > 0:
                    if st[-1] < -a:
                        st.pop()
                    elif st[-1] == -a:
                        st.pop()
                        break
                    else:
                        break
                else:
                    st.append(a)
        return st
