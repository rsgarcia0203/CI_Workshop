class MembershipPlan:
    """
    Clase que representa un plan de membresía.
    """
    def __init__(self, name, base_cost):
        self.name = name
        self.base_cost = base_cost

    def __str__(self):
        return f"{self.name}: ${self.base_cost}"
