class Solution(object):
    def possibleStringCount(self, word):
        n = len(word)
        groups = []
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j

        
        total = 1  

        for count in groups:
            if count > 1:
                total += count - 1

        return total
