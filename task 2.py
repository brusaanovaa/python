class Road:
    length = 0
    width = 0

    def __init__(self, length, width, weight, depth):
        self.length = length
        self.width = width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self.length
        wid = self.width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f"Масса асфальта =\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


r = Road(20, 5000, 25, 5)
r.mass()
