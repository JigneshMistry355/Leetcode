small_string = "ab"
largestring = "pqrs"

word1 = small_string
word2 = largestring

merged = ""
for i in range(len(word1)):
    for j in range(1):
        merged = merged + word1[i]
    for k in range(1):
        merged = merged + word2[i]
            
for i in range(len(word1), len(word2)):
    merged = merged + word2[i]
        
print(merged)

class Solution:
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        return result
    
if __name__ == '__main__':
    object = Solution()
    merged_string = object.mergeAlternately("ab" , "pqrs") 