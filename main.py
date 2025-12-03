
import string

# liste_characters variable contains all lowercase letters from a to z
liste_characters = string.ascii_lowercase

# return the ordinar value of the character in liste_characters variable
def ord(character):
    return liste_characters.index(character)

# return the character correspondant to the number in liste_characters variable
def chr(number):
    return liste_characters[number%26]

# return the crypted or decrypted message depends on the value of parameter cypher
def cesar_sypher(message,key,cipher=True):
   #cipher = True means encrypt the message and False means decrypt the message
    key = key if cipher else -key
    message_result = ""
    for char in message.lower():
        crypted_char = chr((ord(char) + key))
        message_result += crypted_char
    return message_result
    

#return all possible decrypted messages using cesar unsypher function with all possible keys
def hack_cesar_sypher(message_crypted):
   possible_messages=[]
   for possible_key in range(len(liste_characters)):
       possible_messages.append(cesar_sypher(message_crypted,possible_key,cipher = False))
   return possible_messages

#return a message crypted or decrypted function of the parameter cipher 
def vigenere_sypher(message,key,cipher=True):
    cipher = cipher if cipher else False

    message_result = ""    

    for index_char,char in enumerate(message):
        current_key = ord( key[index_char % len(key)] ) 
        crypted_char = cesar_sypher(char,current_key,cipher=cipher)
        message_result += crypted_char
    return message_result


print(vigenere_sypher(message="jftyitvrmjhrooherdpr",key='abbe',cipher = False))  




