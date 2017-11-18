# this problem is similar to 127. Word Ladder
'''
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to "end"),
where ONE mutation is defined as ONE single character changed in the gene string.


For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations.
A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the
minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1
Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2
Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3
'''
from tools import timing
class Solution(object):
    @timing
    def minMutation(self, start, end, bank):
        bank_ = bank[:]
        queue = collections.deque([[start, 0]])
        while queue:
            gene, length = queue.popleft()
            if gene == end:
                return length
            for i in range(len(gene)):
                for c in 'ACGT':
                    if c != gene[i]:
                        next_gene = gene[:i] + c + gene[i+1:]
                        if next_gene in bank_:
                            bank_.remove(next_gene)
                            queue.append([next_gene, length + 1])
        return -1


import collections
class Solution2(object):
    def isMutable(self, gene1, gene2):
        cnt = 0
        for i in range(8):
            if gene1[i] != gene2[i]:
                cnt += 1
                if cnt > 1:
                    return False
        return cnt == 1
    @timing
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = collections.deque()
        queue.append([start, start, 0]) # current, previous, num_steps
        while queue:
            cur, pre, steps = queue.popleft()
            if cur == end:
                return steps
            for gene in bank:
                if self.isMutable(cur, gene) and gene != pre:
                    queue.append([gene, cur, steps+1])
        return -1


start = "AACCGGTT"
end =   "AACCGGTA"
bank = ["AACCGGTA"]

print(Solution().minMutation(start, end, bank))
print(Solution2().minMutation(start, end, bank))


start = "AACCGGTT"
end =   "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(Solution().minMutation(start, end, bank))
print(Solution2().minMutation(start, end, bank))

start = "AAAAACCC"
end =   "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(Solution().minMutation(start, end, bank))
print(Solution2().minMutation(start, end, bank))
