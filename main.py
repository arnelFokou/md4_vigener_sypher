# useful functions used in the project

# ord : is a native function of python that take a character like 'a' or 'B' and give you its 
#       ordinar value in ascii table

# chr : it's the reverse of the function 'ord'. it means that it takes a number in parameter 
#       and give you the correspondant character in ascii table
 
# modulo i 

def cesar_sypher(message,key):
    
    crypted_message = ""
    for character in message:
        position_character_crypted = (ord(character) + key) % 1_114_112
        crypted_character = chr(position_character_crypted)
        crypted_message += crypted_character
    return crypted_message
    
def cesar_unsypher(message,key):
    return cesar_sypher(message,-key)

print(cesar_unsypher(message="fsy~",key=4))