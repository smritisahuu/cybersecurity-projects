# Caesar Cipher Implementation
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# --- User Interaction ---
message = input("Enter your message: ")
shift_value = int(input("Enter shift value (e.g., 3): "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

output = caesar_cipher(message, shift_value, mode)
print(f"\nResult: {output}")
