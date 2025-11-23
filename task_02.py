from collections import deque

def is_it_palindrome(text: str) -> bool:
    # stripping and normalizing string
    cleaned_row = "".join(ch.lower() for ch in text if ch.isalnum())

    # adding symbols into created dequeue
    my_dequeue = deque(cleaned_row)

    # comparing symbols from the both sides
    while len(my_dequeue) > 1:
        if my_dequeue.popleft() != my_dequeue.pop():
            return False

    return True

def show_if_palindrome(text: str):
    print(f"{text} -> {is_it_palindrome(text)}")


# ---- Testing time ----
string1 = "Racecar"
string2 = "Onno"
string3 = "Hello"
string4 = "1b1"
string5 = "my-Ym"

show_if_palindrome(string1)
show_if_palindrome(string2)
show_if_palindrome(string3)
show_if_palindrome(string4)
show_if_palindrome(string5)
