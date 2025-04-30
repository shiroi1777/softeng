def encrypt(message, key):
    result = ""
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += ch
    return result

message = input("Enter a message to encrypt: ")
key = int(input("Enter a key (1-25): "))

encrypted = encrypt(message, key)
print("Encrypted message:", encrypted)