from cryptography.fernet import Fernet
import os 

### LECTURE FICHIER ###

def check_password():
    #open file and read 
    file = open("mypassword.txt", "r")
    key = open("key.txt", "r")

    return

### ECRITURE FICHIER ###

def write_password():
    #Gestion of files
    file = open("mypassword.txt", "a")
    key = open("key.txt", "r")

    #Input
    identifiant = input("Your identifiant : ")
    password = input("Your password : ")

    #Cryptography
    character = key.read()
    ligne = ''
    for ligne in character :
        ligne = character[0]
        for i in range(len(character)):
            if character[i] == '\n':
                ligne += character[i+1]
    
    if ligne != "b" :
        key.close
        key = open("key.txt", "w")
        generate_key = Fernet.generate_key()
        key.writelines(str(generate_key))
        print("Your key is : ",generate_key)
        key.close

    #encrypt the new id and password
    with open('key.txt') as key:
        reader = key.read()
        for row in reader:      #https://stackoverflow.com/questions/53897333/read-fernet-key-causes-valueerror-fernet-key-must-be-32-url-safe-base64-encoded
            used_key = row[0]
            print(Fernet(used_key))
    f = Fernet(used_key)

    encrypt_id = f.encrypt(b,identifiant)
    encrypt_password = f.encrypt(b,password)

    #put encrypted pass and id into the txt
    #file.writelines(encrypt_id+" "+encrypt_password)
    file.close
    return

### MAIN ###

banner = """
`.......                                                            `..
`..    `..                                                          `..
`..    `..   `..     `....  `.... `..     `...   `..    `. `...     `..
`.......   `..  `.. `..    `..     `..  .  `.. `..  `..  `..    `.. `..
`..       `..   `..   `...   `...  `.. `.  `..`..    `.. `..   `.   `..
`..       `..   `..     `..    `.. `. `. `.`.. `..  `..  `..   `.   `..
`..         `.. `...`.. `..`.. `..`...    `...   `..    `...    `.. `..
                                                                       
`..   `..                                               
`..  `..                                                
`.. `..       `..       `..    `. `..     `..    `. `...
`. `.       `.   `..  `.   `.. `.  `..  `.   `..  `..   
`..  `..   `..... `..`..... `..`.   `..`..... `.. `..   
`..   `..  `.        `.        `.. `.. `.         `..   
`..     `..  `....     `....   `..       `....   `...   
                               `..                      

"""
print(banner)
choice= int(input("""1) Look at your password(s)
2) Add password(s)
Choose an option : """))

if choice == 1 :
    check_password()
elif choice == 2 : 
    write_password()