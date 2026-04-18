from algorithms.turning_grille_decrypt import turning_grille_decrypt
from algorithms.turning_grille_encrypt import turning_grille_encrypt
from algorithms.vigenere_decrypt import vigenere_decrypt
from algorithms.vigenere_encrypt import vigenere_encrypt

def use_alg(mode, algorithm, text, key):
    if (algorithm == 'v' and mode == 'enc'):
        print(vigenere_encrypt(text, key))

    elif (algorithm == 'v' and mode == 'dec'):
        print(vigenere_decrypt(text, key))

    elif (algorithm == 't' and mode == 'enc'):
        print(turning_grille_encrypt(text, key))

    else: print(turning_grille_decrypt(text, key))
