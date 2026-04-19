from core.inputs import get_mode, get_algorithm, get_text, get_key, get_size, get_holes
from algorithms.algorithm_control import use_vigenere, use_grille

def start():
    while True:
        mode = get_mode()
        algorithm = get_algorithm()
        if(algorithm == "v"):
            text = get_text()
            key = get_key()
            result = use_vigenere(mode, algorithm, text, key)
        else:
            text = get_text()
            size = get_size()
            holes = get_holes(size)
            result = use_grille(mode, algorithm, text, size, holes)

        print(f"Sending Data, Mode: {mode}, Agorithm: {algorithm}")

        print(result)
        return "END"