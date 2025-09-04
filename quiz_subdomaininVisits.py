class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cnt = defaultdict(int ) 
        for entry in cpdomains : 
            c_str , domain = entry.split()
            c = int(c_str) 
            parts = domain.split('.') 
            for i in range(len(parts ) ) :
                sub = '.'.join(parts[i:]    )
                cnt[sub] += c
        return ['{} {}'.format(v, k) for k, v in cnt.items()]   
