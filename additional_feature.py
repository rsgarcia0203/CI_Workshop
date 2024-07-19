class AdditionalFeature:
    """
    Clase que representa una característica adicional.
    """
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"{self.name}: ${self.cost}"
