class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        maxFreq = 0
        maxLen = 0

        l = 0
        for r in range(len(s)):
            charMap[s[r]] = 1 + charMap.get(s[r], 0)
            maxFreq = max(maxFreq, max(charMap.values()))
            if (r - l + 1) - maxFreq <= k:
                maxLen = max(maxLen, r - l + 1)

            else:
                charMap[s[l]] -= 1
                l += 1

        return maxLen


        