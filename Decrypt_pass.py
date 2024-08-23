import base64


def decrypt(encrypt_str) : 
    encrypted_bytes = base64.b64decode(encrypt_str)
    decode_data = encrypted_bytes.decode()
    print(decode_data)

encrypt_str = input("Enter your encrypted string : ")
decrypt(encrypt_str)
