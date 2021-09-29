'''
nadmiernie skomplikowany randomizer hasel.
'''
import sys, time, random

special_chars = [
    "@",
    "!",
    "%",
    "#",
]
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "w",
    "x",
    "y",
    "z",
]
numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]
words = [
    "scarce",
    "piquant",
    "influence",
    "stimulating",
    "important",
    "puffy",
    "discovery",
    "prose",
    "liquid",
    "appliance",
    "glossy",
    "wonder",
    "thundering",
    "repair",
    "narrow",
    "measly",
    "demonic",
    "disappear",
    "realize",
    "run",
    "warn",
    "new",
    "attend",
    "abandoned",
    "momentous",
    "spiffy",
    "pest",
    "nondescript",
    "advice",
    "swift",
    "chubby",
    "possible",
    "zesty",
    "surround",
    "representative",
    "trashy",
    "abortive",
    "spray",
    "preserve",
    "mix",
    "waste",
    "peep",
    "nutty",
    "overconfident",
    "placid",
]

password = []
program_run = True

def randomize_random(password_length):
    final_password = ''
    cap_character = alphabet[random.randint(0,len(alphabet)-1)]
    cap_character = cap_character.upper()
    s_character = special_chars[random.randint(0,len(special_chars)-1)]
    number = 0
    rand = 0
    character = ""

    for n in range(password_length-2):
        rand = random.randint(1,3)
        if rand == 1 or rand == 2:
            number = numbers[random.randint(0,len(numbers)-1)]
            password.append(number)
        
        elif rand == 3:
            character = alphabet[random.randint(0,len(alphabet)-1)]
            password.append(character)
        
    password.append(s_character)
    password.append(cap_character)

    for i in range(len(password)):
        final_password += password[i]

    password.clear()
    return(final_password)

def randomize_word():
    final_password = ""

    for i in range(0,2):
        number = numbers[random.randint(0,len(numbers)-1)]
        word = words[random.randint(0,len(words)-1)]
        final_password += word
        final_password += number

    return final_password

def randomize_bank(password_length):
    final_password = ""

    for i in range(password_length):
        number = numbers[random.randint(0,len(numbers)-1)]
        final_password += number

    return final_password


print('Type "help" for list of commands')
second_call = 0
while program_run == True:

    cc = input(">>> ")

    if cc == 'help':
        print("Avaliable commands: \n randomize - randomizes your password. \n result - shows you the randomized password. \n save - saves the password to a file. \n read - reads the password save file. \n exit - closes the application.")

    elif cc == 'randomize':
        randomize_type = input('for random password, type "1", for word based password, type "2" and for bank-ready password, type "3" \n >>> ' )
        if randomize_type == '1':
            length = input("how long should the password be? \n >>> ")
            length = int(length)
            password1 = randomize_random(length)
            print("Randomization succsefull.")
        elif randomize_type == '2':
            password1 = randomize_word()
            print("Randomization succsefull.")
        elif randomize_type == '3':
            length = input("how long should the password be? \n >>> ")
            length = int(length)
            password1 = randomize_bank(length)
            print("Randomization succsefull.")
            
    if cc == 'result':
        try:
            print(password1)
        except:
            print('no password generated. use "randomize" to generate one')

    if cc == 'save':
        try:
            print(f"current password: {password1}")
            passfor = input('this is a password for: \n >>> ')
            with open("E:\Programming\Python\password_randomizer\saved_passwords", 'a') as file:
                file.write(passfor + ': ')
                file.write(password1 + '\n')
                print("Password saved succesfully!")
        except:
            print('no password generated. use "randomize" to generate one')
    if cc == 'read':
        f = open("saved_passwords", 'r')
        for word in f:
            print(word)

    if cc == 'exit':
        program_run = False
        sys.exit()
