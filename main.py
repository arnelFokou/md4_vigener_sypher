
import string

# return the crypted or decrypted message depends on the value of parameter cypher
def cesar_sypher(message,key,cipher=True):
   #cipher = True means encrypt the message and False means decrypt the message
    key = key if cipher else -key
    #1_114_112 represents the number of characters presents in utf-8
    message_result = [chr((ord(char) + key) % 1_114_112) for char in message.lower()]
    return "".join(message_result)
    

#return all possible decrypted messages using cesar unsypher function with all possible keys
def hack_cesar_sypher(message_crypted):
   possible_messages=[cesar_sypher(message_crypted,possible_key,cipher = False) for possible_key in range(len(liste_characters)) ]
   return possible_messages

#return a message crypted or decrypted function of the parameter cipher 
def vigenere_sypher(message,key,cipher=True):
    cipher = cipher if cipher else False
    list_of_keys=[ord(char) for char in key]

    message_result = []
    for index_char,char in enumerate(message):
        current_key = list_of_keys[index_char % len(list_of_keys)]
        crypted_char = cesar_sypher(char,current_key,cipher=cipher)
        message_result.append(crypted_char)
    return "".join(message_result)


print(cesar_sypher(message="khoor#zruog",key=3,cipher = False))
#khoor#zruog



