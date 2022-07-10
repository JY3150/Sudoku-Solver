
import json

print("enter solve() to start")
GRID = [[0 for _ in range(9)] for _ in range(9)]


def print_grid(gridx) -> None:
    for _ in range(9):
        print('--', end='')
    print("")
    for i in range(9):
        print("|", end="")
        for j in range(9):
            if (j+1) % 3 == 0:
                print(str(gridx[i][j]), end='|')
            else:
                print(gridx[i][j], end=' ')

        print(f'   ({i+1}) ')
        if (i+1) % 3 == 0:
            for _ in range(9):
                print('--', end='')
            print('')


def create_grid() -> None:
    print("Here's the sudoku template, copy and change it as you need")
    print("[0,0,0|0,0,0|0,0,0]")
    for i in range(9):
        print("please give me the " + str(i+1) + "th line")
        a = input()
        for x in range(1, 18, 2):
            GRID[i][x//2] = int(a[x])
    print("Is this the Sudoku you want to solve?")
    print_grid(GRID)
    print("Enter Y to confirm, Otherwise, enter N")
    b = input()
    while b == "N":
        print("put the lines you want to change in the bracket [], seperate with ,")
        lst = json.loads(input())
        for c in lst:
            print(f'Here is the {c}th line')
            print(f'[{GRID[c - 1][0]},{GRID[c - 1][1]},{GRID[c - 1][2]}|{GRID[c - 1][3]},{GRID[c - 1][4]},{GRID[c - 1][5]}|'
              f'{GRID[c - 1][6]},{GRID[c - 1][7]},{GRID[c - 1][8]}]')
            print("enter the correct line")
            a = input()
            for x in range(1, 18, 2):
                GRID[c - 1][x // 2] = int(a[x])
        print("Here is corrected soduku")
        print_grid(GRID)
        print("enter N if you still want to change, or enter Y to solve your soduku")
        b = input()


def valid(grid, i, j, x) -> bool:
    for a in range(9):
        if a != j and grid[i][a] == x:
            return False
        if a != i and grid[a][j] == x:
            return False

    for a in range(3):
        for b in range(3):
            if grid[i//3 * 3 + a][j//3 * 3 + b] == x and (i//3 * 3 + a, j//3 * 3 + b) != (i, j):
                return False

    return True


def next_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j


def solve_sudoku(grid) -> bool:
    solved = False
    emp = next_empty(grid)

    if emp is None:
        return True
    else:
        r, c = emp

    for x in range(1, 10):

        if valid(grid, r, c, x):
            grid[r][c] = x

            if solve_sudoku(grid):

                solved = True
            else:
                grid[r][c] = 0

    return solved


def solve() -> None:
    create_grid()

    if solve_sudoku(GRID):
        print("Here is the solution")
        print_grid(GRID)
    else:
        print('not solvable')

