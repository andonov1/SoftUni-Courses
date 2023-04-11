from exams.bakery.table.table import Table


class OutsideTable(Table):

    @property
    def min_table_number(self):
        return 51

    @property
    def max_table_number(self):
        return 100

    @property
    def table_message(self):
        return "Outside table's number must be between 51 and 100 inclusive!"
