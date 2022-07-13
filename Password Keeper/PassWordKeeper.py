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
    
    if ligne == "" :
        key.close
        key = open("key.txt", "w")
        generate_key = Fernet.generate_key()
        key.writelines(str(generate_key.decode('utf-8')))
        print("Your key is : ",generate_key)
        key.close

    #encrypt the new id and password
    used_key = open("key.txt", "r")
    keyencrypt = used_key.read()
    used_key.close
    f = Fernet(keyencrypt)

    encrypt_id = f.encrypt(identifiant.encode())
    encrypt_password = f.encrypt(password.encode())
    print("Encrypted id : ",encrypt_id)
    print("Encrypted password : ",encrypt_password)

    #put encrypted pass and id into the txt
    file.writelines(str(encrypt_id.decode('utf-8')))
    file.writelines(str(encrypt_password.decode('utf-8')))
    file.close
    print("New id and password succesfully saved !")
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
