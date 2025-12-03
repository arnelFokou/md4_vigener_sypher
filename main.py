
import string

# liste_characters variable contains all lowercase letters from a to z
liste_characters = string.ascii_lowercase

def ord(character):
    # return the ordinar value of the character in liste_characters variable
    return liste_characters.index(character)

def chr(number):
    # return the character correspondant to the number in liste_characters variable
    return liste_characters[number%26]

def cesar_sypher(message,key):
   #return the crypted message using cesar sypher method with a key
    crypted_message = ""
    for char in message.lower():
        crypted_char = chr((ord(char) + key))
        crypted_message += crypted_char
    return crypted_message
    
def cesar_unsypher(message,key):
    #return the decrypted message using cesar sypher method with a key
    return cesar_sypher(message,-key)

def hack_cesar_sypher(message):
    #return all possible decrypted messages using cesar unsypher function with all possible keys
   possible_values=[]
   for possible_key in range(26):
       possible_values.append(cesar_unsypher(message,-possible_key))
   return possible_values

def length_key_to_length_message(key,missing_length):
    #return a key with the same length as the message
    i=0 #`index to iterate over the key`
    while missing_length > 0:
        key += key[i%26]
        missing_length -= 1
        i+=1
    return key


def vigenere_sypher(message,key,sign=1):
    #sign = 1 for sypher and -1 for unsypher, it helps to respect the DRY principle
    #return the crypted message using vigenere sypher method with a key
    crypted_message = ""
    # if the key length is not equal to the message length
    missing_length = len(message) - len(key)

    if missing_length > 0:
        key = length_key_to_length_message(key,missing_length)
       
    print(key,message)
    for char_msg,char_key in zip(message.lower(),key.lower()):
        crypted_char = chr(ord(char_msg) + ord(char_key) * sign)
        crypted_message +=crypted_char
    return crypted_message

def vigenere_unsypher(message,key):
    decrypted_message = vigenere_sypher(message=message, key=key,sign=-1)
    return decrypted_message


print(vigenere_unsypher(message="ceje",key='cdia'))
# print(string.ascii_letters)


