from exams.bakery.common.food_factory import FoodFactory
from exams.bakery.common.validators import Validator


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

        self.food_factory = FoodFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        if any(x.name == name for x in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self.food_factory.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if any(x.name == name for x in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.food_factory.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({drink_type}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if any(x.table_number == table_number for x in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.food_factory.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if table.is_reserved():
                continue
            if table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def find_food(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food
        return None

    def order_food(self, table_number, *food):
        table = self.find_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered = f"Table {table_number} ordered:\n"
        not_in_menu = f"{self.name} does not have in the menu:\n"

        for food_name in food:
            current_food = self.find_food(food_name)
            if current_food:
                table.order_food(current_food)
                ordered += str(current_food) + '\n'
            else:
                not_in_menu += food_name + '\n'
        return ordered + not_in_menu

    def find_drink(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink
        return None

    def order_drink(self, table_number, *drinks):
        table = self.find_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        ordered = f"Table {table_number} ordered:\n"
        not_in_menu = f"{self.name} does not have in the menu:\n"

        for drink_name in drinks:
            drink = self.find_drink(drink_name)
            if drink:
                table.order_drink(drink)
                ordered += str(drink) + '\n'
            else:
                not_in_menu += drink_name + '\n'
        return ordered + not_in_menu

    def leave_table(self, table_number):
        table = self.find_table(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        info = ''
        for table in self.tables_repository:
            info += table.free_table_info() + '\n'
        return info

    def get_total_income(self):
        for table in self.tables_repository:
            self.total_income += table.get_bill()
        return f"Total income: {self.total_income:.2f}lv"
