class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for word in strs:
            sort = ''.join(sorted(word))
            if sort not in ana:
                ana[sort] = []
            ana[sort].append(word)
        return list(ana.values())