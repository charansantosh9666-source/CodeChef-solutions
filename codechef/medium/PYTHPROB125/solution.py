user_input = input()

book_title, pages_read = user_input.split()

book_title = book_title.lower()

print(f"You have read {pages_read} pages of {book_title}.")
