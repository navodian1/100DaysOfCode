class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1
            if char_count[char] < 0:
                return False

        return all(count == 0 for count in char_count.values())


solution = Solution()
s1 = "listen"
t1 = "silent"
print(f"Question: is given words are anagram?\nAnswer: {solution.isAnagram(s1, t1)}")
