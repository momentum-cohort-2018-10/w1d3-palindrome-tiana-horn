text = input("Please type a sentence or phrase ")

def clean_text(text):
    new_text = ""
    for char in text.lower():
        if char.isalpha():
            new_text = new_text + char
    return new_text

#print(clean_text(text))

# x = 0
# endidx = -1

#     if new_text[x] == new_text[endidx]:
#         idx = idx +1
#         endidx -= 1

def inner(new_text):
    new_text = clean_text(new_text)
    if len(new_text) == 2 and new_text[0] == new_text[-1]:
        return "is a palindrome"
    elif len(new_text) == 1:
        return "is a palindrome"
    if len(new_text) > 1:
        if new_text[0] == new_text[-1]:
            return inner(new_text[1:-1])
        else: 
            return "is not a palindrome"
    else: 
        return "is not a palindrome"

print(inner(text))
