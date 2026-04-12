from core.validation import alg_validation, f_validation, mode, changeKey_request, continue_
from algorithms.turning_grille_decrypt import turning_grille_decrypt
from algorithms.turning_grille_encrypt import turning_grille_encrypt
from algorithms.vigenere_decrypt import vigenere_decrypt
from algorithms.vigenere_encrypt import vigenere_encrypt

def start():
    while True:
        choose_mode = input('Encryption/Decryption (enc/dec): ')
        is_valid, message = mode(choose_mode)

        if is_valid:
            print(message)
            break
        print(message)

    if choose_mode == 'enc':

        plaintext = input ('Plaintext: ')
        key = input('Key: ')

        print('\nV => Vigenere, T => Turning Grille, B => Both.')

        while True:
            algorithm = input("Algorithm (V/T/B): ")
            alg_valid, message = alg_validation(algorithm)

            if alg_valid:

                print(message)

                if algorithm.lower() == 'v':
                    result = vigenere_encrypt(plaintext, key)
                    print(result)
                
                elif algorithm.lower() == 't':
                    result = turning_grille_encrypt(plaintext, key)
                    print(result)

                elif algorithm.lower() == 'b':

                    while True:

                        first = input('Choose first (V/T): ')
                        f_valid, message1 = f_validation(first)

                        if f_valid:
                            print(message1)

                            if first.lower() == 'v':

                                result = vigenere_encrypt(plaintext, key)
                                new_key = changeKey_request()
                                final = turning_grille_encrypt(result, new_key)
                                print(final)

                            else:

                                result = turning_grille_encrypt(plaintext,key)
                                new_key = changeKey_request()
                                final = vigenere_encrypt(result, new_key)
                                print(final)
                                break

                        else:
                            print(message1)
                
                if continue_():
                    start()

                break
            else:
                print(message)
    

    elif choose_mode == 'dec':

        cipherntext = input ('Plaintext: ')
        key = input('Key: ')

        print('\nV => Vigenere, T => Turning Grille, B => Both.')

        while True:
            algorithm = input("Algorithm (V/T/B): ")
            alg_valid, message = alg_validation(algorithm)

            if alg_valid:

                print(message)

                if algorithm.lower() == 'v':
                    result = vigenere_decrypt(cipherntext, key)
                    print(result)
                
                elif algorithm.lower() == 't':
                    result = turning_grille_decrypt(cipherntext, key)
                    print(result)

                elif algorithm.lower() == 'b':

                    while True:

                        first = input('Choose first (V/T): ')
                        f_valid, message1 = f_validation(first)

                        if f_valid:
                            print(message1)

                            if first.lower() == 'v':

                                result = vigenere_decrypt(cipherntext, key)
                                new_key = changeKey_request()
                                final = turning_grille_decrypt(result, new_key)
                                print(final)

                            else:

                                result = turning_grille_decrypt(cipherntext,key)
                                new_key = changeKey_request()
                                final = vigenere_decrypt(result, new_key)
                                print(final)
                            break
                        else:
                            print(message1)
                
                if continue_():
                    start()

                break               
            else:
                print(message)
            