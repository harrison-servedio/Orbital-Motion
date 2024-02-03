
class planet:
    def __init__(self, name, mass, x, y, AX, AY, VX, VY):
        self.name = name
        self.mass = mass
        self.states = [(x, y, AX, AY, VX, VY)]
    