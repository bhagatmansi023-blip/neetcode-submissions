class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for i,j in zip(word1,word2):
            result += i + j
            
        result += word1[len(word2): ]
        result += word2[len(word1): ]
        return result