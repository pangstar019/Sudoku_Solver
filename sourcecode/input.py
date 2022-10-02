def inputpuzzle():
    matrix = []
    print('\n\nInput sudoku puzzle:\nline by line with space between each value\nuse 0 for empty/unknown\nenter "solve" when complete')
    while True:
        row = list(map(str, input().split()))
        if row == ['solve']:
            break
        row = list(map(int, row))
        if len(row) != 9:
            print('\nEnter 9 values per row only.\n\n')
            return False
        matrix.append(row)
    if len(matrix) != 9:
        print('\nFormat error in entered puzzle. 9 by 9 puzzles only.\n\n')
        return False
    return matrix