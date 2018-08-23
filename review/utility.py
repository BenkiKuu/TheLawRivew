import random
import string
import secrets



def generateUniqueKey():
    alphabet = string.ascii_letters + string.digits
    unique_key = ''.join(secrets.choice(alphabet) for i in range(10))
    return unique_key
