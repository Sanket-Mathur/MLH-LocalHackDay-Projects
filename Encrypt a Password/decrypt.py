try:
    key = -(int(input('Enter an integer key: ')) % 256)
    message = input('Enter a encrypted message: ')
except ValueError:
    print('Invalid Input')
    exit()

code = {}
for i in range(256):
    code[chr(i)] = chr((i + key) % 256)

decrypted_message = ''
for i in message[::-1]:
    decrypted_message += code[i]

print(f'Decrypted Message:\n{decrypted_message}')