

# Two pointer for the solution
# Hash map is not efficient to control the pointer
class solution:
    
    def ifcamelMatch(self, query, pattern):
        # define two pointers
        p_idx, p_len = 0, len(pattern)

        for letter in query:
            if p_idx < p_len and letter == pattern[p_idx]:
                p_idx += 1
            elif letter.islower():
                continue
            else:
                return False
        return p_idx == p_len
    
    def camelMatch(self, queries, pattern):
        return [self.ifcamelMatch(query, pattern) for query in queries]
            

