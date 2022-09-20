class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()

        self.assertEqual([], integer._IntegerList__data)

    def test_init_takes_only_int(self):
        integer = IntegerList(3.5, 'Test', 10.2)

        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_correct_data(self):
        integer = IntegerList(2, 4, 5)

        self.assertEqual([2, 4, 5], integer._IntegerList__data)

    def test_get_data_return(self):
        integer = IntegerList(4, 5)
        self.assertEqual([4, 5], integer._IntegerList__data)

        self.assertEqual([4, 5], integer.get_data())

    def test_add_correct_element_to_list(self):
        integer = IntegerList(4, 5)
        self.assertEqual([4, 5], integer._IntegerList__data)

        integer.add(3)
        self.assertEqual([4, 5, 3], integer._IntegerList__data)

    def test_add_element_return(self):
        integer = IntegerList(4, 5)

        self.assertEqual([4, 5, 3], integer.add(3))

    def test_add_element_incorrect_type_float_raise(self):
        integer = IntegerList(4, 5)

        with self.assertRaises(ValueError) as ex:
            integer.add(3.9)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_element_incorrect_type_str_raise(self):
        integer = IntegerList(4, 5)

        with self.assertRaises(ValueError) as ex:
            integer.add('test')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_correct_element_from_list(self):
        integer = IntegerList(4, 5)
        integer.remove_index(0)
        self.assertEqual([5], integer._IntegerList__data)

    def test_remove_element_return(self):
        integer = IntegerList(4, 5)

        self.assertEqual(4, integer.remove_index(0))

    def test_remove_element_index_out_of_range_raise(self):
        integer = IntegerList(4, 5)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_return(self):
        integer = IntegerList(4, 5)

        self.assertEqual(5, integer.get(1))

    def test_get_index_out_of_range_raise(self):
        integer = IntegerList(4, 5)

        with self.assertRaises(IndexError) as ex:
            integer.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_index_out_of_range_raise(self):
        integer = IntegerList(4, 5)

        with self.assertRaises(IndexError) as ex:
            integer.insert(3, 3)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_invalid_value_raise(self):
        integer = IntegerList(4, 5)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, 'test')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_correct_data(self):
        integer = IntegerList(4, 5)

        integer.insert(0, 1)
        self.assertEqual([1, 4, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(4, 5, 100, -100, 90)

        self.assertEqual(100, integer.get_biggest())

    def test_get_index(self):
        integer = IntegerList(4, 5, 100, -100, 90)

        self.assertEqual(4, integer.get_index(90))


if __name__ == "__main__":
    main()
