from algorithms.turning_grille_decrypt import turning_grille_decrypt
from algorithms.turning_grille_encrypt import turning_grille_encrypt
from algorithms.vigenere_decrypt import vigenere_decrypt
from algorithms.vigenere_encrypt import vigenere_encrypt

def use_vigenere(mode, algorithm, text, key):
    if (algorithm == 'v' and mode == 'enc'):
        print(vigenere_encrypt(text, key))
    else: print(vigenere_decrypt(text, key))

def use_grille(mode, algorithm, text, size, holes):
    if (algorithm == 't' and mode == 'enc'):
        print(turning_grille_encrypt(text, size, holes))
    else: print(turning_grille_decrypt(text, size, holes))
