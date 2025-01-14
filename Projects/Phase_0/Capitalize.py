# Taking User Input
user_input = input()

#Blank String
result = ""

# Getting All Words With For Loop
list_of_words = user_input.split()
for words in list_of_words:
    if len(result) > 0:
        result = result + " " + words[0].strip().upper() + words[1:]
    else:
        result = words[0].upper() + words[1:]

print(result)
