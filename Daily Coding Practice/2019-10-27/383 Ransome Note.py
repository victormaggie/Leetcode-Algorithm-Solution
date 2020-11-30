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
            
            if v > mag_zin[k]:   # if not exist in magazine, it will return 0
                return False

            # if mag_zin.get(k, None) == None:
            #     return False
            # elif mag_zin.get(k) < v:
            #     return False
        return True

        #  complexity: o(1)
    
    def canConstruct_2(self, ransomNote, magazine):
        hash_table = collections.defaultdict(str)

        for letter in magazine:
            hash_table[letter] = hash_table[letter] + 1 if letter in hash_table else 1
        
        for i in ransomNote:
            if i not in hash_table:
                return False
            else:
                hash_table[i] -= 1
                if hash_table[i] < 0:
                    return False
        return True

        # complexity o(1)

    def canConstruct_3(self, ransomNote, magazine):
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
