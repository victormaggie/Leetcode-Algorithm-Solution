class Solution(object):
    def letterCombinations(self, digits):
        """
        iterative solution, update the list
        """
        dict_dial = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        res = [""]
        # edge case
        if digits == "":
            return None
        
        for j in digits:
            temp = []   # update the original list
            for m in dict_dial[int(j)]:
                for n in res:
                    n += m
                    temp.append(n)
            res = temp
        return res


class Solution2(object):
    def letterCombinations(self, digits):
        """
        back-tracking and dfs
        """
        res = []
        path = ''
        self.dfs(digits, 0, res, path)
        return res
    
    def dfs(self, digits, count, res, path):

        dict_dial = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",   
            9: "wxyz"
        }

        # edge case
        if digits == "":
            return None

        if len(digits) == count:
            res.append(path)
            return
        
        else:
            for i in dict_dial[int(digits[count])]:
                path = path + i
                self.dfs(digits, count + 1, res, path)
                path = path[:-1]
                # clear the body.
        
        