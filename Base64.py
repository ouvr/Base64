import base64,os

#clear

os.system('clear')

# input

message = input("\nMasukkan Teks : ")

# clear

os.system('clear')

# Text -> Base64

message_bytes = message.encode('ascii')

base64_bytes = base64.b64encode(message_bytes)

base64_message = base64_bytes.decode('ascii')

print('\nTEXT -> BASE 64')

print('BASE64 : ', base64_message)

# Base64 -> Text

base64_bytes = base64_message.encode('ascii')

message_bytes = base64.b64decode(base64_bytes)

message = message_bytes.decode('ascii')

print('\nBASE64 -> TEXT')

print('TEXT   : ', message)

# creator

print('\nCreate By Mozz\n')
