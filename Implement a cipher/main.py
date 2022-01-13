try:
    plaintext = input('Enter the plaintext: ')
    shift = int(input('Enter the shift: '))
except ValueError:
    print('Non numeric shift entered.')
    exit()

cipher = ''
for c in plaintext:
    if c.isupper():
        cipher += chr((ord(c) - 65 + shift) % 26 + 65)
    else:
        cipher += chr((ord(c) - 97 + shift) % 26 + 97)

print('The ciphertext is:', cipher)