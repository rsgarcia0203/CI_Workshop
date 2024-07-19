from membership_plan import MembershipPlan
from additional_feature import AdditionalFeature

class MembershipManager:
    """
    Clase que maneja la gestión de membresías.
    """
    def __init__(self):
        self.membership_plans = {
            'Basic': MembershipPlan('Basic', 50),
            'Premium': MembershipPlan('Premium', 100),
            'Family': MembershipPlan('Family', 150)
        }

        self.additional_features = {
            'Personal Training': AdditionalFeature('Personal Training', 30),
            'Group Classes': AdditionalFeature('Group Classes', 20),
            'Exclusive Facilities': AdditionalFeature('Exclusive Facilities', 50),
            'Specialized Programs': AdditionalFeature('Specialized Programs', 40)
        }

    def display_membership_plans(self):
        """
        Muestra los planes de membresía disponibles.
        """
        print("Available Membership Plans:")
        for plan in self.membership_plans.values():
            print(f"- {plan}")

    def display_additional_features(self):
        """
        Muestra las características adicionales disponibles.
        """
        print("Available Additional Features:")
        for feature in self.additional_features.values():
            print(f"- {feature}")

    def select_membership_plan(self):
        """
        Permite al usuario seleccionar un plan de membresía.
        """
        self.display_membership_plans()
        while True:
            plan_name = input("Select a membership plan: ").strip()
            if plan_name in self.membership_plans:
                return self.membership_plans[plan_name]
            print("Invalid plan selection. Please choose again.")

    def select_additional_features(self):
        """
        Permite al usuario seleccionar características adicionales.
        """
        selected_features = []
        self.display_additional_features()
        while True:
            feature_name = input("Select an additional feature (enter to skip): ").strip()
            if feature_name == "":
                break
            if feature_name in self.additional_features:
                selected_features.append(self.additional_features[feature_name])
            else:
                print("Invalid feature selection. Please choose again.")
        return selected_features

    def calculate_membership_cost(self, plan, selected_features):
        """
        Calcula el costo total de la membresía.
        """
        base_cost = plan.base_cost
        features_cost = sum(feature.cost for feature in selected_features)
        total_cost = base_cost + features_cost

        if len(selected_features) >= 2:
            total_cost *= 0.9

        if total_cost > 400:
            total_cost -= 50
        elif total_cost > 200:
            total_cost -= 20

        if plan.name == 'Premium' or any(
                feature.name in ['Exclusive Facilities', 'Specialized Programs'] for feature in selected_features):
            total_cost *= 1.15

        return total_cost

    def confirm_membership(self, plan, selected_features, total_cost):
        """
        Confirma la membresía seleccionada.
        """
        print(f"\nSelected Membership Plan: {plan.name}")
        print("Selected Additional Features:")
        for feature in selected_features:
            print(f"- {feature.name}")
        print(f"Total Cost: ${total_cost}")

        confirm = input("\nConfirm membership? (yes/no): ").strip().lower()
        if confirm == 'yes':
            return total_cost
        return -1
