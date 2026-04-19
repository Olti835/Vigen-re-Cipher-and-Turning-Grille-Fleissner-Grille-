def mode(choose_mode):
    choose_mode = choose_mode.lower()

    if choose_mode in ('enc', 'dec'):
        return True, '\nContinue'
    
    return False, "\nInvalid input. Use enc or dec."


def alg_validation(algorithm):
    algorithm = algorithm.lower()

    if algorithm in ('v', 't'):
        return True, "Good. \n"

    return False, "\nInvalid input. Use V or T."
 
def validate_holes(holes, size):
    if not isinstance(holes, list):
        return False, "Holes must be a list of tuples."

    for item in holes:
        if not isinstance(item, tuple) or len(item) != 2:
            return False, "Each hole must be a tuple (row, col)."

        r, c = item

        if not isinstance(r, int) or not isinstance(c, int):
            return False, "Row and column must be integers."

        if r < 0 or c < 0 or r >= size or c >= size:
            return False, "Hole coordinates out of grid bounds."

    return True, "Valid holes"
