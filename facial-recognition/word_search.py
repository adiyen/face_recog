f = open("test.txt")
doc = f.read()
words = doc.split()

count = 0
search = ""
running = True
while running:
    letter = input(f"Please type a letter:{search}")
    search += letter[0]
    count += 1
    for word in words:
        if search == word[0:count]:
            print(word)
#     running = False
# print("no word found")