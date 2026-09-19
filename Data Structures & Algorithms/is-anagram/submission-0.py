class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for letter in s:
        #     for let in t:
        #         if letter is not let:
        #             return False
        s1 = "".join(sorted(s))
        t1 = "".join(sorted(t))

        if s1 == t1:
            return True
        return False