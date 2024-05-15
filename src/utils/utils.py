import bcrypt

salt=bcrypt.gensalt()
def encode_password(new_password:str):
    strValue = bcrypt.hashpw(new_password.encode(), salt).decode('UTF-8')
    return strValue


def verify_password(password, old_password):
    hashed_pass = bcrypt.hashpw(password.encode(), salt).decode('UTF-8')
    return hashed_pass==old_password
