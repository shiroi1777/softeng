def decrypt(message, key):
    result = ""
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base - key + 26) % 26 + base
            result += chr(shifted)
        else:
            result += ch
    return result

message = input("Enter a message to decrypt: ")
key = int(input("Enter the key used for encryption (1-25): "))

decrypted = decrypt(message, key)
print("Decrypted message:", decrypted)
