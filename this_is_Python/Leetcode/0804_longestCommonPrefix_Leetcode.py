class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        return shortest

lcp = Solution()
print(lcp.longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(lcp.longestCommonPrefix(strs=["dog", "racecar", "car"]))