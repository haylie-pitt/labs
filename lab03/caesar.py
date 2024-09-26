class Caesar:
    def __init__(self):
        self._key = 0  # Private attribute for the key

    def get_key(self):
        return self._key

    def set_key(self, key):
        self._key = key

    # Encrypt the plaintext using the Caesar Cipher
    def encrypt(self, plaintext):
        ciphertext = []
        for char in plaintext:
            if char.isalpha():  # Check if the character is a letter
                # Shift within the bounds of lowercase letters
                shifted_char = chr(((ord(char.lower()) - ord('a') + self._key) % 26) + ord('a'))
                ciphertext.append(shifted_char)
            elif char.isspace():  # Keep whitespace unchanged
                ciphertext.append(char)
            else:  # Handle special characters by shifting their ASCII values
                shifted_char = chr(ord(char) + self._key)
                ciphertext.append(shifted_char)
        return ''.join(ciphertext)

    # Decrypt the ciphertext using the Caesar Cipher
    def decrypt(self, ciphertext):
        plaintext = []
        for char in ciphertext:
            if char.isalpha():  # Check if the character is a letter
                # Shift back within the bounds of lowercase letters
                shifted_char = chr(((ord(char.lower()) - ord('a') - self._key) % 26) + ord('a'))
                plaintext.append(shifted_char)
            elif char.isspace():  # Keep whitespace unchanged
                plaintext.append(char)
            else:  # Handle special characters by shifting their ASCII values back
                shifted_char = chr(ord(char) - self._key)
                plaintext.append(shifted_char)
        return ''.join(plaintext)

# Example
if __name__ == "__main__":
    cipher = Caesar()

    cipher.set_key(3)
    print(cipher.encrypt("hello WORLD!"))  # prints "khoor zruog$"
    print(cipher.decrypt("KHOOR zruog$"))  # prints "hello world!"

    cipher.set_key(6)
    print(cipher.encrypt("zzz"))  # prints "fff"
    print(cipher.decrypt("FFF"))  # prints "zzz"

    cipher.set_key(-6)  # Negative keys should be supported!
    print(cipher.encrypt("FFF"))  # prints "zzz"
