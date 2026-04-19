from core.inputs import get_mode, get_algorithm, get_text, get_key, get_size, get_holes
from algorithms.algorithm_control import use_alg

def start():
    while True:
        mode = get_mode()
        algorithm = get_algorithm()
        if(algorithm == "v"):
            text = get_text()
            key = get_key()
        else:
            text = get_text()
            size = get_size()
            holes = get_holes(size)

        
        print(f"Sending Data, Mode: {mode}, Agorithm: {algorithm}")
        result = use_alg(mode, algorithm, text, key)

        print(result)
        return "END"