'''
LIFE FOR TWO

Competitive Game of Life (two or more players).

Ported by Sajid Sarker (2022).
'''

# Global Variable Initialisation
# Initialise the board
gn = [[0 for _ in range(6)] for _ in range(6)]
gx = [0 for _ in range(3)]
gy = [0 for _ in range(3)]
gk = [0, 3, 102, 103, 120, 130, 121,
      112, 111, 12, 21, 30, 1020, 1030,
      1011, 1021, 1003, 1002, 1012]
ga = [0, -1, 0, 1, 0, 0, -1, 0, 1, -1, -1, 1, -1, -1, 1, 1, 1]
m2 = 0
m3 = 0


# Helper Functions
def tab(number) -> str:
    t = ""
    while len(t) < number:
        t += " "
    return t


def display_header() -> None:
    print(f"{tab(33)}LIFE2")
    print(f"{tab(15)}CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY\n\n\n")
    print(f"{tab(10)}U.B. LIFE GAME")


# Board Functions
def setup_board() -> None:
    # Players add symbols to initially setup the board
    for b in range(1, 3):
        p1 = 3 if b != 2 else 30
        print(f"\nPLAYER {b} - 3 LIVE PIECES.")
        for _ in range(1, 4):
            query_player(b)
            gn[gx[b]][gy[b]] = p1


def modify_board() -> None:
    # Players take turns to add symbols and modify the board
    for b in range(1, 3):
        print(f"PLAYER {b} ")
        query_player(b)
        if b == 99:
            break
    if b <= 2:
        gn[gx[1]][gy[1]] = 100
        gn[gx[2]][gy[2]] = 1000


def simulate_board() -> None:
    # Simulate the board for one step
    for j in range(1, 6):
        for k in range(1, 6):
            if gn[j][k] > 99:
                b = 1 if gn[j][k] <= 999 else 10
                for o1 in range(1, 16, 2):
                    gn[j + ga[o1] - 1][k + ga[o1 + 1] - 1] += b
                    # gn[j+ga[o1]][k+ga[o1+1]-1] = gn[j+ga[o1]][k+ga[o1+1]]+b


def display_board() -> None:
    # Draws the board with all symbols
    m2, m3 = 0, 0
    for j in range(7):
        print("")
        for k in range(7):
            if j in [0, 6]:
                if k != 6:
                    print(f" {str(k)} ", end="")
                else:
                    print(" 0 ", end="")
            elif k in [0, 6]:
                print(f" {str(j)} ", end="")
            elif gn[j][k] < 3:
                gn[j][k] = 0
                print("   ", end="")
            else:
                for o1 in range(1, 19):
                    if gn[j][k] == gk[o1]:
                        break
                if o1 <= 18:
                    if o1 > 9:
                        gn[j][k] = 1000
                        m3 += 1
                        print(" # ", end="")
                    else:
                        gn[j][k] = 100
                        m2 += 1
                        print(" * ", end="")
                else:
                    gn[j][k] = 0
                    print("   ", end="")


# Player Functions
def query_player(b) -> None:
    # Query player for symbol placement coordinates
    while True:
        print("X,Y\nXXXXXX\n$$$$$$\n&&&&&&")
        a_ = input("??")
        b_ = input("???")
        x_ = [int(num) for num in a_.split() if num.isdigit()]
        y_ = [int(num) for num in b_.split() if num.isdigit()]
        x_ = x_ or [0]
        y_ = y_ or [0]
        gx[b] = y_[0]
        gy[b] = x_[0]
        if gx[b] in range(1, 6)\
                and gy[b] in range(1, 6)\
                and gn[gx[b]][gy[b]] == 0:
            break
        print("ILLEGAL COORDS. RETYPE")
    if b != 1 and gx[1] == gx[2] and gy[1] == gy[2]:
        print("SAME COORD. SET TO 0")
        gn[gx[b] + 1][gy[b] + 1] = 0
        b = 99


# Game Functions
def check_winner(m2, m3) -> None:
    # Check if the game has been won
    if m2 == 0 and m3 == 0:
        print("\nA DRAW\n")
        return
    if m3 == 0:
        print("\nPLAYER 1 IS THE WINNER\n")
        return
    if m2 == 0:
        print("\nPLAYER 2 IS THE WINNER\n")
        return


# Program Flow
def main() -> None:
    display_header()
    setup_board()
    display_board()
    while True:
        print("\n")
        simulate_board()
        display_board()
        check_winner(m2, m3)
        modify_board()


if __name__ == "__main__":
    main()
