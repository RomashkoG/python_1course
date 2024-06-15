class Vector:
    def __init__(self, components):
        self.components = components

    def vector(self):
        return self.components  

    def dim(self):
        return len(self.components)
    
    def length(self):
        return sum(el ** 2 for el in self.components) ** 0.5
    
    def average(self):
        return sum(self.components) / len(self.components)

    def max_comp(self):
        return max(self.components) if self.components else 0

    def min_comp(self):
        return min(self.components) if self.components else 0


def max_dimension(vectors):
    max_dim = 0
    vec_max_dim = None
    for vec in vectors:
        if max_dim < vec.dim():
            max_dim = vec.dim()
            vec_max_dim = vec
        elif max_dim == vec.dim():
            if vec_max_dim.length() > vec.length():
                vec_max_dim = vec
    return vec_max_dim.vector()

def max_length(vectors):
    max_length = 0
    vec_max_length = None
    for vec in vectors:
        if max_length < vec.length():
            max_length = vec.length()
            vec_max_length = vec
        elif max_length == vec.length():
            if vec_max_length.dim() < vec.dim():
                vec_max_length = vec
    return vec_max_length.vector()

def average_length(vectors):
    vectors_length = [vec.length() for vec in vectors]
    return sum(vectors_length) / len(vectors)

def above_average_length(vectors):
    avg_length = average_length(vectors)
    above_average = 0
    for vec in vectors:
        if vec.length() > avg_length:
            above_average += 1
    return above_average

def max_component(vectors):
    max_component = 0
    for vec in vectors:
        if max_component < vec.max_comp():
            max_component = vec.max_comp()
            vec_max_comp = vec
        elif max_component == vec.max_comp():
            if vec_max_comp.min_comp() > vec.min_comp():
                vec_max_comp = vec
    return vec_max_comp.vector()

def min_component(vectors):
    min_component = 0
    for vec in vectors:
        if min_component > vec.min_comp():
            min_component = vec.min_comp()
            vec_min_comp = vec
        elif min_component == vec.min_comp():
            if vec_min_comp.max_comp() < vec.max_comp():
                vec_min_comp = vec
    return vec_min_comp.vector()

def read_file(file_name):
    vectors = []
    with open(file_name, 'r') as file:
        for line in file:
            vectors.append(list(map(int, line.split())))
    return vectors

def generator(vectors):
    return [Vector(vec) for vec in vectors]

if __name__ == "__main__":
    file_names = ["input01.txt", "input02.txt", "input03.txt", "input04.txt"]

    for file_name in file_names:
        vectors = generator(read_file(file_name))
        print(f"{file_name}\n")
        print("Найбільша розмірність:", max_dimension(vectors))
        print("Найбільша довжина:", max_length(vectors))
        print("Середня довжина:", average_length(vectors))
        print("Більші за Середню довжину:", above_average_length(vectors))
        print("Максимальна компонета:", max_component(vectors))
        print("Мінімальна компонента:", min_component(vectors))
