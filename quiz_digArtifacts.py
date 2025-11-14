class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        dug = set((r, c) for r, c in dig)
        count = 0
        for r1, c1, r2, c2 in artifacts:
            ok = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                count += 1
        return count
