sentence = input("Enter sentence")

final_sentence = ""

for letter in sentence:
    if(letter.isupper()):
        final_sentence = final_sentence + letter.lower()
    elif(letter.islower()):
            final_sentence = final_sentence + letter.upper()
    else:
        final_sentence = final_sentence + letter
        
print(final_sentence)