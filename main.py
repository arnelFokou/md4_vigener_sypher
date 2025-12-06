
import string

# string.printable is a string that contains all printable characters in python, i choose dictinnary to reduce spatial complexity
ascii_index_char = { index:char  for index, char in enumerate(string.printable) }
ascii_char_index = {char:index for index,char in ascii_index_char.items()}


def ord(char):
    return ascii_char_index[char]

def chr(num):
    return ascii_index_char[num % len(ascii_index_char)]

# return the crypted or decrypted message depends on the value of parameter cypher
def cesar_sypher(message,key,cipher=True):

   #cipher = True means encrypt the message and False means decrypt the message
    key = key if cipher else -key

    message_crypted = [ chr(ord(char) + key) for char in message]

    return "".join(message_crypted)
    

#return all possible decrypted messages using cesar unsypher function with all possible keys
def hack_cesar_sypher(message_crypted):
   possible_messages=[cesar_sypher(message_crypted,possible_key,cipher = False) for possible_key in range(len(ascii_index_char)) ]
   return possible_messages

   
#return a message crypted or decrypted function of the parameter cipher 
def vigener_sypher(message,key,cipher=True):
    cipher = cipher if cipher else False
    list_of_keys=[ord(char) for char in key]
   

    message_crypted = []
    for index_char,char in enumerate(message):
        current_key = list_of_keys[index_char % len(list_of_keys)]
        
        crypted_char = cesar_sypher(message=char,key=current_key,cipher=cipher)

        message_crypted.append(crypted_char)
    return "".join(message_crypted)



# msg = vigener_sypher(message="RzGJyfRMBGy]4EziCPDQ4PIC4AzKwz",key="allo",cipher=False)
# print(msg)

msg=cesar_sypher(message="Hello World",key=5,cipher=True)
possible_msg = hack_cesar_sypher(message_crypted=msg)
print(possible_msg)





