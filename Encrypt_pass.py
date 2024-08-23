import base64


def encrypt(password) : 
    encrypted_bytes = base64.b64encode(password.encode())
    print(encrypted_bytes)

user_pass = input("Enter your Password : ")
encrypt(user_pass)