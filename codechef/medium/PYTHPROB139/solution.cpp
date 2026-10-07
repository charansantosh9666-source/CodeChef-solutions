user_input = input()

leading_cleaned = user_input.lstrip()

trailing_cleaned = user_input.rstrip()

fully_cleaned = user_input.strip()

print(f"Original Address: '{user_input}'")
print(f"After lstrip(): '{leading_cleaned}'")  
print(f"After rstrip(): '{trailing_cleaned}'")  
print(f"After strip(): '{fully_cleaned}'")      