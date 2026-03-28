sentence = "I speak Goat Latin"
vowels = ["a", "e", "i", "o", "u"]
output = []
sentence = [i for i in sentence.split()]
print(sentence)
for i in range(len(sentence)):
    temp = ""
    print(sentence[i][0])
    if sentence[i][0].lower() in vowels:
        temp = sentence[i] + "ma"
        temp = temp  + (i+1)* "a"
    else:
        temp = sentence[i][1:] + sentence[i][0] +  "ma"
        temp = temp  + (i+1)* "a"
    output.append(temp)
    temp = ""

print(" ".join(str(i) for i in output))