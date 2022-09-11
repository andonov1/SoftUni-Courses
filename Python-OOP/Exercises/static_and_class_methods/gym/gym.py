class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if self.__find_item(customer, self.customers) is None:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if self.__find_item(trainer, self.trainers) is None:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if self.__find_item(equipment, self.equipment) is None:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if self.__find_item(plan, self.plans) is None:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if self.__find_item(subscription, self.subscriptions) is None:
            self.subscriptions.append(subscription)

    def __find_item(self, item, location):
        for current_item in location:
            return current_item

    def subscription_info(self, subscription_id):
        subscription = self.__find_entity_by_id(subscription_id, self.subscriptions)
        customer = self.__find_entity_by_id(subscription.customer_id, self.customers)
        trainer = self.__find_entity_by_id(subscription.trainer_id, self.trainers)
        plan = self.__find_entity_by_id(subscription.exercise_id, self.plans)
        equipment = self.__find_entity_by_id(plan.equipment_id, self.equipment)
        return f'{repr(subscription)}\n' \
               f'{repr(customer)}\n' \
               f'{repr(trainer)}\n' \
               f'{repr(equipment)}\n' \
               f'{repr(plan)}'

    def __find_entity_by_id(self, id, collection):
        for item in collection:
            if item.id == id:
                return item
