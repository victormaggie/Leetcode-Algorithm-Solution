class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        # use the word justification method

        def process(row, maxWidth, total):
            
            # check if its the last word
            if len(row) == 1:
                return ' '.join(row) + ' '*(maxWidth - total)
            
            # if we have more than one word
            gaps = (maxWidth - total) // (len(row)-1)

            # the residual space calculation
            missing = (maxWidth - gaps * (len(row)-1) - total)

            # distribute the missing value to the words
            for i in range(missing):
                row[i] += ' '
            
            # contribute the new word builder
            return ((' '*gaps) .join(row))
        
        row = []
        total = 0
        ans = []
        for word in words:

            # determine how many words can be build in a line
            # the maxWidth that can be present here
            if len(word) + total + len(row) > maxWidth:
                ans.append(process(row, maxWidth, total))
                row = [word]
                total = len(word)
            
            else:
                row.append(word)
                total += len(word)

            # be aware of case like ['aabb' , 'ccdd']
            ans.append(process([' '.join(word)], maxWidth, total+len(row)-1))
            return ans

# time complexity o( n )
# space complexity o(n)

