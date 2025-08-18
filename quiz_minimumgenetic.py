class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        from collections import deque

        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        genes = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for ch in genes:
                    if ch != gene[i]:
                        new_gene = gene[:i] + ch + gene[i+1:]
                        if new_gene in bank_set:
                            bank_set.remove(new_gene)
                            queue.append((new_gene, steps + 1))

        return -1

