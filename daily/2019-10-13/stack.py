## related programming question

# No. 1 check the balanced parenthesis

    # process the parenthesis string from left to right.
    # if symbol is an opening parenthesis, push it on the stack.
    # if symbol is an closing parenthesis. pop it out the stack.
    # if stack is empty, then balanced parathesis. 

# check the Parenthesis all like "(((())))"

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()

        index = index + 1
    return True

# check the balanced symbols "{}, [], ()"

def balanced_checker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    return False
        index += 1
    
    return True

def matches(open, close):
    open = "([{"
    close = "}])"
    return open.index(open) == close.index(close)  # check the index no need dict


class Stack():
    def __init__(self):
        self.Stack = []

    def push(self, item):
        self.Stack.append(item)

    def pop(self):
        return self.Stack.pop()

    def peek(self):
        return self.Stack[-1]
    
    def isEmpty(self):
        return self.Stack == []

    def size(self):
        return len(self.Stack)