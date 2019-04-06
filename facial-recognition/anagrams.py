# anagram:  star, rats.  car, arc - anagrams
word1 = input("Please enter your first word: ")
word2 = input("Please enter your second word: ")

numb1 = []
numb2 = []

running = True

for ch in word1:
    numb1.append(ch)

for ch in word2:
    numb2.append(ch)
while running:
    if len(word1) != len(word2):
        print("These 2 words are not anagrams.")
        running = False


    for i in range(len(word1)):
        if numb1[i] in numb2:
            running = True
        else:
            running = False
            break
    break

if running == False:
    print("These 2 words are not anagrams.")
else:
    print("These 2 words are anagrams.")

