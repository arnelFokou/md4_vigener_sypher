
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

print(hack_cesar_sypher(message="psmgdsy"))
# print(string.ascii_letters)


