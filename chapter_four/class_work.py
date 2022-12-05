word = "Hello boss baby"
to_be_found = "b"
for i in range(len(word)):

    if word[i] == to_be_found:
        print(f"{word[i]:<2} was found at index {i:>2}")
        print({i})
print()

for letter in word:
    if letter != "b":
        print(letter, end="")
print()

for index, value in enumerate(word):
    print("value->", value, "index->", index, end=" ")
