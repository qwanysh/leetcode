class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}
        mapped_words = set()

        for i in range(len(pattern)):
            if pattern[i] not in mapping:
                if words[i] in mapped_words:
                    return False

                mapping[pattern[i]] = words[i]
                mapped_words.add(words[i])
                continue

            if mapping[pattern[i]] != words[i]:
                return False

        return True
