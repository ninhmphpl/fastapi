from datetime import datetime, timedelta
from jose import JWTError, jwt
import time

SECRET_KEY = "09d25e094faa6ca1999c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECOND = 1

def create_jwt():
    expire = datetime.utcnow() + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECOND)
    token = jwt.encode(claims={'key': 'value', 'username' : 'ninh', 'exp' : expire}, key=SECRET_KEY, algorithm='HS256')
    print(token)
    return token

def decode_jwt(token):
    try:
        claims = jwt.decode(token=token,key=SECRET_KEY,algorithms="HS256")
        print(claims)
    except JWTError as e:
        print(e)

token = create_jwt()
time.sleep(2)
decode_jwt(token)




