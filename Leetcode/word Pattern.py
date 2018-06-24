class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) == len(words):
            return len(set(zip(pattern,words))) == len(set(pattern)) == len(set(words))
        else:
            return False