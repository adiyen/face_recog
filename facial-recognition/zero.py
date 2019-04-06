word = input("Enter the string ZERO as many times as you want: ")

numb = []
word_count = 0

start = 0
for i in range(len(word)//4):
    numb.append(word[start:start+4])
    start+=4
    #print(numb[i])
    if numb[i] == "ZERO":
        word_count +=1
print(word_count)
