class Stack:
    """CopyPaste from Class Notes"""
    def __init__(self):
        self.stack = []

    # Add element to stack
    def push(self, item):
        self.stack.append(item)

    # Removing element from stack
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # checking is stack empty
    def is_empty(self):
        return len(self.stack) == 0

    # checking last stack's element
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]


def check_delimiters(text: str) -> str:
    stack = Stack()

    opening = "([{"
    closing = ")]}"
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        # for opening bracket
        if char in opening:
            stack.push(char)

        # for closing bracket
        elif char in closing:
            if stack.is_empty():
                return "Symetrical"

            top = stack.pop()

            # if types of brackets is different
            if pairs[char] != top:
                return "Non-symetrical"

    # check if stack empty to define symmetry
    if not stack.is_empty():
        return "Non-symetrical"

    return "Symetrical"

def show_if_symetrical(text: str) -> str:
    print(f"{text}: {check_delimiters(text)}")


# ---- Testing time ----
row1 =  "( ){[ 1 ]( 1 + 3 )( ){ }}"
row2 =  "( 23 ( 2 - 3);"
row3 =  "( ){[ 1 ]( 1 + 3 )( ){ }}"
show_if_symetrical(row1)
show_if_symetrical(row2)
show_if_symetrical(row3)
