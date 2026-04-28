from algorithms.turning_grille_decrypt import turning_grille_decrypt
from algorithms.turning_grille_encrypt import turning_grille_encrypt
from algorithms.vigenere_decrypt import vigenere_decrypt
from algorithms.vigenere_encrypt import vigenere_encrypt

def use_vigenere(mode, algorithm, text, key):
    if (algorithm == 'v' and mode == 'enc'):
        ciphertext = vigenere_encrypt(text, key)
        print(ciphertext)
    else: 
        plaintext = vigenere_decrypt(text, key)
        print(plaintext)

def use_grille(mode, algorithm, text, size, holes):
    if (algorithm == 't' and mode == 'enc'):
        ciphertext = turning_grille_encrypt(text, size, holes)
        print(ciphertext)
    else:
        plaintext = turning_grille_decrypt(text, size, holes)
        print(plaintext)
