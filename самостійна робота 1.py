import random
def print_field(field):
    print('--------' * len(field[0]))
    for row in field:
        res = '   |   '.join(row)
        res = f"|   {res}   |"
        print(res)
        print('--------' * len(row))

def move_player():
    while True:
        print("Зробити хід ↓")
        n = input("В якому рядку: ")
        n1 = input("В якому стовпчику: ")

        try:
            n, n1 = int(n), int(n1)
        except ValueError:
            print("Неправильний ввід")

        if (n and n1) not in (1, 2, 3):
            print("Неправильний ввід")

        elif field[n - 1][n1 - 1] == " ":
            field[n - 1][n1 - 1] = 'x'
            break

        else:
            print("Тут сюди походити не можна")

def move_computer():
    empty_el = []
    for i, j in enumerate(field):
        for j, value in enumerate(j):
            if value == " ":
                empty_el.append((i, j))
    n, n1 = random.choice(empty_el)
    field[n][n1] = 'o'

field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

while True:
    print_field(field)
    move_player()
    move_computer()
