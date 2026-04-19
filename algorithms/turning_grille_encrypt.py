def turning_grille_encrypt(plaintext, size, holes):
    # Krijo matricën bosh
    grid = [["" for _ in range(size)] for _ in range(size)]

    # Funksion ndihmës për rrotullim 90°
    def rotate_holes(holes):
        return [(c, size - 1 - r) for r, c in holes]

    # Mbush matricën me shkronjat e plaintext-it sipas vrimave
    idx = 0
    current_holes = holes
    for _ in range(4):
        current_holes.sort()
        for r, c in current_holes:
            if idx < len(plaintext):
                grid[r][c] = plaintext[idx]
                idx += 1
        current_holes = rotate_holes(current_holes)

    # Bashko matricën në një string (ciphertext)
    ciphertext = "".join("".join(row) for row in grid)
    return ciphertext
