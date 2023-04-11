from exams.bakery.baked_food.bread import Bread
from exams.bakery.baked_food.cake import Cake
from exams.bakery.drink.tea import Tea
from exams.bakery.drink.water import Water
from exams.bakery.table.inside_table import InsideTable
from exams.bakery.table.outside_table import OutsideTable


class FoodFactory:
    food_types = {'Cake': Cake,
                  'Bread': Bread
                  }

    drinks_types = {'Tea': Tea,
                    'Water': Water
                    }

    table_types = {'InsideTable': InsideTable,
                   'OutsideTable': OutsideTable
                   }

    def create_food(self, food_type, name, price):
        return self.__class__.food_types[food_type](name, price)

    def create_drink(self, drink_type, name, portion, brand):
        return self.__class__.drinks_types[drink_type](name, portion, brand)

    def create_table(self, table_type, table_number, capacity):
        return self.__class__.table_types[table_type](table_number, capacity)