def is_complete(queens,size):
    return len(queens)==size

def place_next(queens,size):
    next_queens = []
    for i in range(size):
        if not i in queens:
            next_queens.append(queens+[i])
    return next_queens

def print_queens(queens,size) : 
    for i in range(len(queens)) : # Kein enhenced-for mehr, damit wir die Indizes haben
        print(str(size-i)+'   '*queens[i],' Q')  # Reihenname an den Anfang der Zeile schreiben, Rest ist wie zuvor auch
    letters = " " #Untere Spaltenbeschriftung mit Buchstaben
    for i in range(size):
        letters += "  " + chr(ord('A')+i)
    print(letters)

def diags_safe(queens,size):
    for i in range(len(queens)):
        for j in range(i+1,len(queens)):
            if abs(queens[i]-queens[j])==j-i:
                return False
    return True 

def solve(queens,size):
    if is_complete(queens,size):
        print(queens)
        print_queens(queens)
        return True
    else:
        next_queens = place_next(queens,size)
        i = 0
        solveable = False
        while not solveable and i<len(next_queens):
            if diags_safe(next_queens[i],size):
                solveable = solve(next_queens[i],size)
            i = i+1
        return solveable

def solve_all(queens,size):
    if is_complete(queens,size):
        return [queens]
    else:
        next_queens = place_next(queens,size)

        solutions = []
        for stat in next_queens:
            if diags_safe(stat,size):
                solutions += solve_all(stat,size)
        return solutions

size = 8
sols = solve_all([],size)
for sol in sols:
    print_queens(sol,size)
print("Lösungen insgesamt: " + str(len(sols)))

