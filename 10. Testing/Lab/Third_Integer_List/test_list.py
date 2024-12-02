from unittest import TestCase, main

# from Third_Integer_List.list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList(6.7 , 1,2,3,4 , "wow")

    def test_correct_init(self):
        self.assertEqual([1,2,3,4],self.integer_list.get_data())

    def test_add_returns_correct_data(self):
        expected_list = self.integer_list.get_data() + [5]

        self.integer_list.add(5)

        self.assertEqual(expected_list,self.integer_list.get_data())

    def test_add_not_integer_added_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.integer_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_remove_index_expect_correct_data(self):
        self.integer_list.remove_index(0)

        self.assertEqual([2,3,4], self.integer_list.get_data())

    def test_remove_incorrect_index_expect_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(6)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_expect_correct_index(self):
        self.integer_list.get(2)

        self.assertEqual(3, self.integer_list.get_data()[2])

    def test_get_with_incorrect_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(8)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_valid_index_expect_correct_data(self):
        expected_list = self.integer_list.get_data().copy()

        expected_list.insert(0, 3)
        self.integer_list.insert(0, 3)

        self.assertEqual(expected_list,self.integer_list.get_data())

    def test_insert_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(7, 6)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_invalid_not_integer_index_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(2, 5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest_expect_biggest_number(self):
        expected_result = self.integer_list.get_biggest()
        self.assertEqual(4, expected_result)

    def test_get_index_returns_correct_index(self):
        result = self.integer_list.get_index(2)

        self.assertEqual(1, result)

if __name__ == "__main__":
    main()