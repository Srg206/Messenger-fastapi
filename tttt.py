import bcrypt

salt=bcrypt.gensalt()
def encode_password(new_password:str):
    strValue = bcrypt.hashpw(new_password.encode(), salt).decode('UTF-8')
    return strValue

print(encode_password("123"))
print(bcrypt.hashpw(("123").encode(), salt))