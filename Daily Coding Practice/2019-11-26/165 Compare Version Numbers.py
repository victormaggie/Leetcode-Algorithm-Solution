class Solution:
    def compareVersion(self, version1, version2):
        version1 = self.get_num(version1)
        version2 = self.get_num(version2)

        if version1 < version2: return -1
        elif version1 > version2: return 1
        else: return 0

    def get_num(self, version):
        res = []
        i = 0
        while i < len(version):
            # local variable
            j = i
            s = 0
            if (j < len(version) and version[j] != '.'):
                while (j < len(version) and version[j] != '.'):
                    s = s * 10 + int(version[j])
                    j += 1
                i = j
                res.append(s)
            
            else:
                i += 1
            
        while (len(res) and res[-1] == 0): res.pop()
        return res

# o(n)