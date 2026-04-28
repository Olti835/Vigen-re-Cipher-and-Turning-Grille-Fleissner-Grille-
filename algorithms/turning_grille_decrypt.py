def turning_grille_decrypt(ciphertext, size, holes):
    # Krijo matricën dhe mbushe me ciphertext
    grid = []
    idx = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(ciphertext[idx])
            idx += 1
        grid.append(row)

    def rotate_holes(holes):
        return [(c, size - 1 - r) for r, c in holes]

    plaintext = ""
    current_holes = holes

    for _ in range(4):
        current_holes.sort()
        for r, c in current_holes:
            plaintext += grid[r][c]
        current_holes = rotate_holes(current_holes)

    return f"Plaintext: {plaintext}"