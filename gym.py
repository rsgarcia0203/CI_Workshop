"""
Módulo de gestión de membresías para el gimnasio.
"""

membership_plans = {
    'Basic': {'base_cost': 50},
    'Premium': {'base_cost': 100},
    'Family': {'base_cost': 150}
}

additional_features = {
    'Personal Training': 30,
    'Group Classes': 20,
    'Exclusive Facilities': 50,
    'Specialized Programs': 40
}

def display_membership_plans():
    """
    Muestra los planes de membresía disponibles.
    """
    print("Available Membership Plans:")
    for plan, details in membership_plans.items():
        print(f"- {plan}: ${details['base_cost']}")

def display_additional_features():
    """
    Muestra las características adicionales disponibles.
    """
    print("Available Additional Features:")
    for feature, cost in additional_features.items():
        print(f"- {feature}: ${cost}")

def select_membership_plan():
    """
    Permite al usuario seleccionar un plan de membresía.
    """
    display_membership_plans()
    while True:
        plan = input("Select a membership plan: ").strip()
        if plan in membership_plans:
            return plan
        print("Invalid plan selection. Please choose again.")

def select_additional_features():
    """
    Permite al usuario seleccionar características adicionales.
    """
    selected_features = []
    display_additional_features()
    while True:
        feature = input("Select an additional feature (enter to skip): ").strip()
        if feature == "":
            break
        if feature in additional_features:
            selected_features.append(feature)
        else:
            print("Invalid feature selection. Please choose again.")
    return selected_features

def calculate_membership_cost(plan, selected_features):
    """
    Calcula el costo total de la membresía.
    """
    base_cost = membership_plans[plan]['base_cost']
    features_cost = sum(additional_features[feature] for feature in selected_features)
    total_cost = base_cost + features_cost

    if len(selected_features) >= 2:
        total_cost *= 0.9 

    if total_cost > 400:
        total_cost -= 50
    elif total_cost > 200:
        total_cost -= 20

    if plan == 'Premium' or any(
            feature in selected_features for feature in ['Exclusive Facilities', 'Specialized Programs']):
        total_cost *= 1.15 

    return total_cost

def confirm_membership(plan, selected_features, total_cost):
    """
    Confirma la membresía seleccionada.
    """
    print(f"\nSelected Membership Plan: {plan}")
    print("Selected Additional Features:")
    for feature in selected_features:
        print(f"- {feature}")
    print(f"Total Cost: ${total_cost}")

    confirm = input("\nConfirm membership? (yes/no): ").strip().lower()
    if confirm == 'yes':
        return total_cost
    return -1

def main():
    """
    Función principal que maneja el flujo del programa.
    """
    print("Welcome to the Gym Membership Management System!")

    plan = select_membership_plan()

    selected_features = select_additional_features()

    total_cost = calculate_membership_cost(plan, selected_features)

    result = confirm_membership(plan, selected_features, total_cost)
    if result != -1:
        print(f"\nThank you! Your total membership cost is: ${result}")
    else:
        print("Membership cancellation or invalid input detected. Process canceled.")

if __name__ == "__main__":
    main()
