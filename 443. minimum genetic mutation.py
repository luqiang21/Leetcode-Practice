# this problem is similar to 127. Word Ladder, http://www.cnblogs.com/grandyang/p/7653006.html
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


'''
[Analysis]
The gene strings can construct a graph with each node is an gene and each edge
is a valid mutation. Then the problem becomes find a path from start node to the end node.
This can be done with BFS and time complexity is O(N).

The construction of the graph needs to compare every two nodes, which makes the
time complexity O(N^2). Since the gene string is an 8-character string with only 4 letters,
 instead of constructing a graph, we can use all valid mutation of a given string when
 probing the next possible gene. There only 31(4x8-1) possibilities. Therefore,
the overall time complexity can be still O(N).
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

import collections
def toNumber(gene):
    table = {v:i for i, v in enumerate('ATGC')}
    return sum([table[letter] * 1 << (2 * i) for i, letter in enumerate(gene)])

@timing
def findMutationDistance(start, end, bank):
    bank = set(map(toNumber, bank))
    start = toNumber(start)
    end = toNumber(end)
    queue = [(start, 0)]
    visited = set([start])
    while queue:
        gene, steps = queue.pop(0)
        if gene == end:
            return steps
        for x in range(8):
            for y in range(4):
                next = gene ^ (y << (x * 2))
                if next in bank and next not in visited:
                    visited.add(next)
                    queue.append((next, steps+1))
    return -1

start = "AACCGGTT"
end =   "AACCGGTA"
bank = ["AACCGGTA"]

print(Solution().minMutation(start, end, bank))
print(Solution2().minMutation(start, end, bank))
print(findMutationDistance(start, end, bank))

start = "AACCGGTT"
end =   "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(Solution().minMutation(start, end, bank))
print(Solution2().minMutation(start, end, bank))
print(findMutationDistance(start, end, bank))

start = "AAAAACCC"
end =   "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
print(Solution().minMutation(start, end, bank))
print(Solution2().minMutation(start, end, bank))
print(findMutationDistance(start, end, bank))
