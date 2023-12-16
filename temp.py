def caesar_cipher(text, shift):
    encrypted_text = ''
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

name = 'Ahmed'
shift = 3
encrypted_name = caesar_cipher(name, shift)
print(encrypted_name) 







