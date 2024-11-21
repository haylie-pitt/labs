def shift_character(ch, shift, alphabet):
    """Shift a single character."""
    if ch in alphabet:
        new_pos = (alphabet.index(ch) + shift) % len(alphabet)
        return alphabet[new_pos]
    return ch

def caesar_encrypt(text, shift):
    """Encrypt the text using Caesar Cipher."""
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet_lower.upper()

    return ''.join(
        shift_character(ch, shift, alphabet_lower if ch.islower() else alphabet_upper)
        if ch.isalpha() else ch for ch in text
    )

def caesar_decrypt(text, shift):
    """Decrypt the text using Caesar Cipher."""
    return caesar_encrypt(text, -shift)

# Testing
if __name__ == "__main__":
    plaintext = "Hello, World!"
    shift = 3
    encrypted = caesar_encrypt(plaintext, shift)
    print(f"Encrypted: {encrypted}")  # Output: "Khoor, Zruog!"
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")  # Output: "Hello, World!"
