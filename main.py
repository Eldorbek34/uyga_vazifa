def removeStars(word):
    stack = []
    for char in word:
        if char == '*':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
word = input("So'zni kiriting: ")
natija = removeStars(word)
print("Natija:", natija)
