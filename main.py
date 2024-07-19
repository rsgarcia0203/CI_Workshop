from membership_manager import MembershipManager

def main():
    """
    Función principal que maneja el flujo del programa.
    """
    print("Welcome to the Gym Membership Management System!")

    manager = MembershipManager()

    plan = manager.select_membership_plan()

    selected_features = manager.select_additional_features()

    total_cost = manager.calculate_membership_cost(plan, selected_features)

    result = manager.confirm_membership(plan, selected_features, total_cost)
    if result != -1:
        print(f"\nThank you! Your total membership cost is: ${result}")
    else:
        print("Membership cancellation or invalid input detected. Process canceled.")

if __name__ == "__main__":
    main()
