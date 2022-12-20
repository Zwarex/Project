from cryptography.fernet import Fernet
import os 
import csv

### LECTURE FICHIER ###

def check_password():
    #open file and read 
    file = open("mypassword.txt", "r")
    key = open("key.txt", "r")

    #take  content of the file
    content = file.read().split("/")
    content.pop()
    
    #decrypt
    compteur = 0
    keydecrypt = key.read()
    f = Fernet(keydecrypt)
    for i in content : #parcourir un par un les elements
        i_bytes = bytes(i, 'UTF-8') 
        encrypt_pass = i_bytes
        decrypted_pass = f.decrypt(encrypt_pass).decode()
        if compteur%2 == 0:
            print("The ID : ",decrypted_pass)
        else :
            print("The password : ",decrypted_pass)
        compteur +=1

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
    file.write(str(encrypt_id.decode('UTF-8'))) #.decode("utf-8")
    file.write("/")
    file.write(str(encrypt_password.decode('UTF-8')))
    file.write("/")
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
