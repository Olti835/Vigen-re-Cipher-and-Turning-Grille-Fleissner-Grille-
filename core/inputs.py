from core.validation import mode, alg_validation

def get_text():
    m = input("Text: ")
    return m

def get_key():
    m = input("Key: ")
    return m

def get_mode():
    while True:
        m = input('enc/dec: ')
        valid, msg = mode(m)
        print(msg)
        if valid:
            return m
        
def get_algorithm():
    print("\nV -> Vgenere, t -> Turning Grille")
    while True:
        m = input('Choose algorithm v/t: ')
        valid, msg = alg_validation(m)
        print(msg)
        if valid:
            return m
