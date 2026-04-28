from core.validation import mode, alg_validation, validate_holes, validate_size

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
    print("\nv -> Vgenere, t -> Turning Grille")
    while True:
        m = input('Choose algorithm v/t: ')
        valid, msg = alg_validation(m)
        print(msg)
        if valid:
            return m.lower()
        
def get_size():
    while True:
        m = input("Size: ")
        valid, size, msg = validate_size(m)
        print(msg)

        if valid:
            return size 
        
def get_holes(size):
    while True:
        raw = input("Enter holes (e.g. (0,1),(1,3),(2,0)): ")

        try:
            holes = []

            # Heq hapësirat
            raw = raw.replace(" ", "")

            # Ndaj tuples
            parts = raw.split("),")

            for p in parts:
                p = p.replace("(", "").replace(")", "")
                r, c = p.split(",")

                holes.append((int(r), int(c)))

            valid, msg = validate_holes(holes, size)
            print(msg)

            if valid:
                return holes

        except Exception:
            print("\nInvalid format. Example: (0,1),(1,3),(2,0)")
