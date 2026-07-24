class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank=set(bank)
        queue = [
            (startGene, 0)
        ]
        visited = {startGene}
        while queue:
            current, mutations = queue.pop(0)
            if current==endGene:
                return mutations
            for i in range(len(current)):
                for ch in ['A','C','G','T']:
                    s = list(current)
                    if ch == s[i]:
                        continue
                    s[i]=ch
                    new_gene="".join(s)
                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, mutations + 1))
        return -1