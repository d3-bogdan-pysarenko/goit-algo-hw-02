class Stack:
    def __init__(self):
        self.stack = []

# Додавання елемента до стеку
def push(self, item):
    self.stack.append(item)

# Видалення елемента зі стеку
def pop(self):
    if len(self.stack) < 1:
        return None
    return self.stack.pop()

# Перевірка, чи стек порожній
def is_empty(self):
    return len(self.stack) == 0

# Перегляд верхнього елемента стеку без його видалення
def peek(self):
    if not self.is_empty():
        return self.stack[-1]






def check_delimiters(text: str) -> str:
    stack = Stack()

    opening = "([{"
    closing = ")]}"
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        # Якщо відкрита дужка
        if char in opening:
            stack.push(char)

        # Якщо закрита дужка
        elif char in closing:
            if stack.is_empty():
                return "Несиметрично"

            top = stack.pop()

            # Якщо типи дужок не співпадають
            if pairs[char] != top:
                return "Несиметрично"

    # Після проходу рядка стек має бути порожній
    if not stack.is_empty():
        return "Несиметрично"

    return "Симетрично"


# ---- Приклади ----
tests = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for t in tests:
    print(f"{t}: {check_delimiters(t)}")
    