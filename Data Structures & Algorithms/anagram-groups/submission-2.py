class Solution:
    def groupAnagrams(self, strs):
        dic = {}

        for word in strs:
            key = tuple(sorted(word))

            if key not in dic:
                dic[key] = []

            dic[key].append(word)

        return list(dic.values())