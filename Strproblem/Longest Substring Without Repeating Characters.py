class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        strarr = []
        strstack = ''
        for i in range(len(s)):
            strstack = strstack + s[i]

            strarr.append(strstack)

        return strarr






a = Solution()

s = 'abcabcbb'
print(a.lengthOfLongestSubstring(s))

