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

def validate_size(size):
    try:
        size = int(size)
        return True, size, "\nSize validated."
    except ValueError:
        return False, None, "Invalid size. Write an integer value."
 
def validate_holes(holes, size):
    if not isinstance(holes, list):
        return False, "Holes must be a list of tuples."

    expected = (size * size) // 4
    if len(holes) != expected:
        return False, f"Number of holes must be {expected} for a {size}x{size} grid."

    seen = set()

    for item in holes:
        if not isinstance(item, tuple) or len(item) != 2:
            return False, "Each hole must be a tuple (row, col)."

        r, c = item

        if not isinstance(r, int) or not isinstance(c, int):
            return False, "Row and column must be integers."

        if r < 0 or c < 0 or r >= size or c >= size:
            return False, "Hole coordinates out of grid bounds."

        if (r, c) in seen:
            return False, "Duplicate hole detected."
        seen.add((r, c))

    def rotate(hs):
        return [(c, size - 1 - r) for r, c in hs]

    all_positions = set()
    current = holes

    for _ in range(4):
        for pos in current:
            if pos in all_positions:
                return False, "Invalid grille: holes overlap during rotation."
            all_positions.add(pos)
        current = rotate(current)

    if len(all_positions) != size * size:
        return False, "Invalid grille: does not cover entire grid."

    return True, "Valid holes"
