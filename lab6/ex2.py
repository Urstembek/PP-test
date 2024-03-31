def count_cases(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

s = "Hello World"
upper_count, lower_count = count_cases(s)
print(f"Upper case letters: {upper_count}, Lower case letters: {lower_count}")