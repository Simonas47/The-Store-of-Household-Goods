
class Fridge:
    def __init__ (self, name, id, volume, energyClass, installation, color, freezer, price, height, width, depth):
        self.name = name
        self.id = id
        self.volume = volume
        self.energyClass = energyClass
        self.installation = installation
        self.color = color
        self.freezer = freezer
        self.price = price
        self.height = height
        self.width = width
        self.depth = depth

    def __eq__(self, other):
        if not isinstance(other, Fridge):
            return NotImplemented
        return self.id == other.id

