try:
    key = int(input('Enter an integer key: ')) % 256
    message = input('Enter a message to encrypt: ')
except ValueError:
    print('Invalid Input')
    exit()

code = {}
for i in range(256):
    code[chr(i)] = chr((i + key) % 256)

encrypted_message = ''
for i in message[::-1]:
    encrypted_message += code[i]

print(f'Encrypted Message:\n{encrypted_message}')