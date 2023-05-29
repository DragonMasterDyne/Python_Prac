# First, let's define the Furniture class
class Furniture:
    def __init__(self, width, height, material):
        self.width = width
        self.height = height
        self.material = material

class Surface:
    def __init__(self, flat):
        self.flat = flat

class Table(Furniture, Surface):
    def __init__(self, width = 0, height = 0, material = "Wood", flat = True):
        Furniture.__init__(self, width, height, material)
        Surface.__init__(self, flat)
        self.legs = 4

# Next, let's define the Chair class
class Chair(Furniture):
    def __init__(self, material,  width = 0, height = 0, arms = True, back = True):
        super().__init__(width, height, material)
        self.arms = arms
        self.back = back

    def fold(self):
        self.folded = True
        print("The chair is now folded and ready for transport.")

    def unfold(self):
        self.folded = False
        print("The chair is now unfolded and ready for use.")

class Bench(Chair):
    pass
# sofa = Bench("Metal")
# print(vars(sofa))

a = Table()
print(vars(a))