def check_delimiters(text: str) -> str:
    stack = []
    opening = "([{"
    closing = ")]}"
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in text:
        # якщо символ — відкрита дужка → додаємо у стек
        if char in opening:
            stack.append(char)

        # якщо символ — закрита дужка → перевіряємо
        elif char in closing:
            # якщо стек порожній — немає відповідної відкритої
            if not stack:
                return "Несиметрично"

            top = stack.pop()

            # перевіряємо, чи відповідає тип дужки
            if pairs[char] != top:
                return "Несиметрично"

    # після проходу рядка стек має бути порожнім
    if stack:
        return "Несиметрично"

    return "Симетрично"


# ---- Приклади використання ----
tests = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for t in tests:
    print(f"{t}: {check_delimiters(t)}")
