from core.inputs import get_mode, get_algorithm, get_text, get_key
from algorithms.algorithm_control import use_alg

def start():
    while True:
        mode = get_mode()
        text = get_text()
        key = get_key()
        algorithm = get_algorithm()
        
        print(f"Sending Data, Mode: {mode}, Agorithm: {algorithm}")
        result = use_alg(mode, algorithm, text, key)

        print(result)
        return "END"