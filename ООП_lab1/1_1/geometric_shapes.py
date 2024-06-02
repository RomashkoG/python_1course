class Figure:

    def perimeter(self):
        pass

    def area(self):
        pass

    def exsists(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if not self.exsistance():
            raise ValueError(f"Трикутника {self.a}, {self.b}.")

    def perimeter(self):
        return(self.a + self.b + self.c)
    
    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def exsistance(self):
        if self.a < 0 or self.b < 0 or self.c < 0 or self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
            return False
        else:
            return True

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

        if not self.exsistance():
            raise ValueError(f"Прямокутника {self.a}, {self.b} не існує")

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def exsistance(self):
        if self.a < 0 or self.b < 0:
            return False
        else:
            return True


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        if not self.exsistance():
            raise ValueError(f"Трапеції {self.a}, {self.b}, {self.c}, {self.d} не існує")

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c) * (p - self.d)) ** 0.5

    def exsistance(self):
        if self.a < 0 or self.b < 0 or self.c < 0 or self.d < 0 or self.a == self.b or self.a + self.b + self.c < self.d or self.a + self.d + self.c < self.b or self.a + self.b + self.d < self.c or self.d + self.b + self.c < self.a:
            return False
        else:
            return True

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

        if not self.exsistance():
            raise ValueError(f"Паралелограма {self.a}, {self.b}, {self.h} не існує")

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.b * self.h

    def exsistance(self):
        if self.a < 0 or self.b < 0 or self.h < 0:
            return False
        else:
            return True


class Circle(Figure):
    def __init__(self, r):
        self.r = r

        if not self.exsistance():
            raise ValueError(f"Фігури з такими параметрами не існує")

    def perimeter(self):
        return 2 * 3.14 * self.r

    def area(self):
        return 3.14 * (self.r ** 2)

    def exsistance(self):
        if self.r < 0:
            return False
        else:
            return True


shapes = {
    "Triangle": Triangle,
    "Rectangle": Rectangle,
    "Trapeze": Trapeze,
    "Parallelogram": Parallelogram,
    "Circle": Circle
}

def figure_generator(line):
    name = line[0]
    numbers = line[1:]
    shape = shapes[name]
    class_numbers = []
    for num in numbers:
        class_numbers.append(int(num))
    return shape(*class_numbers)

def max_perimeter(figures: list):
    max_per = 0
    for figure in figures:
        max_per = max(figure.perimeter(), max_per)
    return max_per

def max_area(figures: list):
    max_ar = 0
    for figure in figures:
        max_ar = max(figure.area(), max_ar)
    return max_ar

if __name__ == "__main__":
    file_name = input("Введіть назву імені файлу: ")
    figures = []
    with open(file_name) as file:
        for line in file:
            try:
                figures.append(figure_generator(line.split()))
            except ValueError:
                pass

    print(max_perimeter(figures))
    print(max_area(figures))