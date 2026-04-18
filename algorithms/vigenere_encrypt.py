def vigenere_encrypt(ciphertext, key):
    ciphertext = ciphertext.strip().upper()
    key = key.strip().upper()

    key = (key * ((len(ciphertext) // len(key)) + 1))[:len(ciphertext)]

    plaintext = ""

    for k,c in zip(key, ciphertext):
            c = ord(c) - 65
            k = ord(k) - 65

            z = ((c+k)%26) + 65
            plaintext += chr(z) 

    return f"Plaintext: {plaintext}"