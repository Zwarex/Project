from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
print(f)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(token)
print(f.decrypt(token))