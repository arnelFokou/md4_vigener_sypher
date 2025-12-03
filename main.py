
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
    crypted_message = ""
    for char in message.lower():
        crypted_char = chr((ord(char) + key))
        crypted_message += crypted_char
    return crypted_message
    

# def hack_cesar_sypher(message):
#     #return all possible decrypted messages using cesar unsypher function with all possible keys
#    possible_values=[]
#    for possible_key in range(26):
#        possible_values.append(cesar_unsypher(message,-possible_key))
#    return possible_values

# def length_key_to_length_message(key,missing_length):
#     #return a key with the same length as the message
#     i=0 #`index to iterate over the key`
#     while missing_length > 0:
#         key += key[i%26]
#         missing_length -= 1
#         i+=1
#     return key


# def vigenere_sypher(message,key):
#     #return the crypted message using vigenere sypher method with a key
#     crypted_message = ""
#     # if the key length is not equal to the message length
#     missing_length = len(message) - len(key)

#     if missing_length > 0:
#         key = length_key_to_length_message(key,missing_length)
       
#     for char_msg,char_key in zip(message.lower(),key.lower()):
#         crypted_char = cesar_sypher(char_msg,ord(char_key))
#         crypted_message +=crypted_char
#     return crypted_message

# def vigenere_unsypher(message,key):

#     #return the decrypted message using cesar unsipher function with a key
#     decrypted_message = ""
#     # if the key length is not equal to the message length
#     missing_length = len(message) - len(key)

#     if missing_length > 0:
#         key = length_key_to_length_message(key,missing_length)
       
#     for char_msg,char_key in zip(message.lower(),key.lower()):
#         crypted_char = cesar_sypher(char_msg,ord(char_key))
#         crypted_message +=crypted_char
#     return crypted_message

#     decrypted_message = vigenere_sypher(message=message, key=key)
#     return decrypted_message


#print(vigenere_unsypher(message="ceje",key='cdia'))
print(cesar_sypher(message="dchuwb",key=3,cipher=False))  # khoor



