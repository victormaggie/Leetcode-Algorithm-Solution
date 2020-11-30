# write a fizz buzz
# This question, we use the or operand for the non-bolean operation

# for non-boolean, or will return the first True value

class Solution:
    def fizzBuzz(self, n):

        return ['Fizz' * (not i%3) + 'Buzz' * (not i%5) or str(i) for i in range(1, n+1)]


    # brute force method
    def fizzBuzz_2(self, n):
        
        res = []
        for i in range(1, n+1):
            
            if i%3 == 0 and i%5 == 0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 ==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res