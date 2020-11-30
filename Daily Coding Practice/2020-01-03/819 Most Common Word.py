class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import collections
        if paragraph == '':
            return
        for c in "!?',.:":
            paragraph = paragraph.replace(c, ' ')
        common = collections.Counter(map(lambda x: x.lower(), paragraph.split())).most_common()

        for i in common:
            key, fre = i
            if str(key) in banned:
                continue
            else:
                return key

# time complexity: o(P+B)
# space complexity: O(P+B)


    def mostCommonWord1(self, paragraph, banned):
        import re
        import collections
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
    

    def mostCommonWorld2(self, paragraph, banned):
        import collections
        if paragraph == '':
            return
        for c in '!?,.:':
            paragraph = paragraph.replace(c, ' ')
        common = collections.Counter(i for i in paragraph.split() if i not in banned).most_common(1)
        return common[0][0]

