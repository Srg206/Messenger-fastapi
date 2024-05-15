import bcrypt

salt=bcrypt.gensalt()
def encode_password(new_password:str):
    print("START ENCODE")
    strValue = bcrypt.hashpw(new_password.encode(), salt).decode('UTF-8')
    print(new_password)
    print(strValue)
    print("FINISH ENCODE") 
    return strValue


def verify_password(password, old_password):
    print("VERIFY")
    hashed_pass = encode_password(password)
    print(hashed_pass)
    print(old_password)
    return hashed_pass==old_password
