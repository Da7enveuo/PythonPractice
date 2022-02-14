import hashlib
username = 'password'
byte_uname = username.encode('utf-8')
h_uname = hashlib.sha512(byte_uname)
hashed_username = h_uname.hexdigest()
print(hashed_username)
