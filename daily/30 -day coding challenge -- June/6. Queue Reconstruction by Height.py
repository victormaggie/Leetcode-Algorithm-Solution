class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # here we use the reverse = True, descending order
        # then use the negative order
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output

# use the insert (index, value) into the list