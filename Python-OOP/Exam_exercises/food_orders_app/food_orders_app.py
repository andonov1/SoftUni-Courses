from robots_manager.client import Client
from robots_manager.meals.meal import Meal


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        valid_meals = ["Starter", "MainDish", "Dessert"]
        for meal in meals:
            if meal.__class__.__name__ in valid_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = ''
        for meal in self.menu:
            result += meal.details() + '\n'
        return result.strip()

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = None
        client_registered = False
        for client in self.clients_list:
            if client_phone_number == client.phone_number:
                client_registered = True
        if not client_registered:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        ordered_meals = {}
        for meal_name, quantity in meal_names_and_quantities.items():
            meal_in_menu = False
            for meal in self.menu:
                if meal_name == meal.name:
                    meal_in_menu = True
                    if meal.quantity < quantity:
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
                    ordered_meals[meal] = quantity

            if not meal_in_menu:
                raise Exception(f"{meal_name} is not on the menu!")

        for meal, quantity in ordered_meals.items():
            for menu_meal in self.menu:
                if meal.name == menu_meal.name:
                    menu_meal.quantity -= quantity
            client.shopping_cart.append(meal)
            client.bill += meal.price * quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(x.name for x in ordered_meals)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = None
        for current in self.clients_list:
            if client_phone_number == current.phone_number:
                client = current

        if len(client.shopping_cart) < 1:
            raise Exception("There are no ordered meals!")

        while client.shopping_cart:
            meal = client.shopping_cart.pop()
            for current_meal in self.menu:
                if meal.name == current_meal.name:
                    current_meal.quantity += meal.quantity
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = None
        for current_client in self.clients_list:
            if current_client.phone_number == client_phone_number:
                client = current_client

        if len(client.shopping_cart) < 1:
            raise Exception("There are no ordered meals!")

        paid = client.bill
        client.bill = 0
        client.shopping_cart = []
        FoodOrdersApp.RECEIPT_ID += 1
        return f"Receipt #{FoodOrdersApp.RECEIPT_ID} with total amount of {paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
