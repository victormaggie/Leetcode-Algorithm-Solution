class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import collections
        if paragraph == '':
            return
        for c in "!?',.:":
            paragraph.replace(c, ' ')
        common = collections.Counter(map(lambda x: x.lower(), paragraph.split())).most_common()

        for i in common:
            key, fre = i
            if str(key) in banned:
                continue
            else:
                return key

# time complexity: o(P+B)
# space complexity: O(P+B)
