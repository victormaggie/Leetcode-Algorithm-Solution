# This question is:

# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazine

# This question only need consider that frequency --- Hash Tablel Solution
import collections
class Solution:
    def canConstruct(self, ransomNote, magazine):

        # build-in formula

        ran_som = collections.Counter(ransomNote)
        mag_zin = collections.Counter(magazine)

        for k, v in ran_som.items():
            if mag_zin.get(k, None) == None:
                return False
            elif mag_zin.get(k) < v:
                return False
        return True