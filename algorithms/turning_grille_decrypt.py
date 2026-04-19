def turning_grille_decrypt(ciphertext, size, holes):
    # Krijo matricën nga teksti i koduar
    grid = []
    for i in range(0, len(ciphertext), size):
        grid.append(list(ciphertext[i : i + size]))

    result = []
    current_holes = holes

    # Funksion ndihmës për rrotullim 90°
    def rotate_holes(holes):
        return [(c, size - 1 - r) for r, c in holes]

    # Lexo për 4 rrotullime
    for _ in range(4):
        current_holes.sort()
        for r, c in current_holes:
            result.append(grid[r][c])
        current_holes = rotate_holes(current_holes)

    return "".join(result).strip()
