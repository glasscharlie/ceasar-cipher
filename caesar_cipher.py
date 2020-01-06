# from nltk.corpus import words
# word_list = words.words()

def encrypt(text, s): 
    result = ''
  
    for i in range(len(text)): 
        char = text[i] 
  
        if (char.isupper()): 
            result += chr((ord(char) + s - 65) % 26 + 65) 
  
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 



def decrypt(text, s): 
    test = 26 - s
    result = ''
  
    for i in range(len(text)): 
        char = text[i] 
  
        if (char.isupper()): 
            result += chr((ord(char) + test - 65) % 26 + 65) 
  
        else: 
            result += chr((ord(char) + test - 97) % 26 + 97) 
  
    return result 
  



test = encrypt('testonetwothreefourfivesix', 5)
print(test)

print(decrypt(test, 5))