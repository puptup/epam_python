import unittest
import Tasks

class TestTasks(unittest.TestCase):

    # 1.1
    def test_calculate_lenght_of_string(self):
        self.assertEqual(Tasks.calculate_lenght_of_string(
        "abcdefg"),
        7)
    
    # 1.2
    def test_character_frequency(self):
        self.assertEqual(Tasks.character_frequency(
        'Oh, it is python'),
        {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1})

    # 1.3
    def test_sorting_unique_words(self):
        self.assertEqual(Tasks.sorting_unique_words(
        ['red', 'white', 'black', 'red', 'green', 'black']),
        ['black', 'green', 'red', 'white'])

    # 1.4
    def test_divisor(self):
        self.assertEqual(Tasks.divisor(
        60),
        [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60])

    # 1.5
    def test_sort_dict_by_key(self):
        self.assertEqual(Tasks.sort_dict_by_key(
        {'1':1,'33':2,'America':3,'Brat':4,'Cyber':5,'2':6}),
        [('1', 1), ('2', 6), ('33', 2), ('America', 3), ('Brat', 4), ('Cyber', 5)])

    # 1.6
    def test_convert_tuple(self):
        self.assertEqual(Tasks.convert_tuple(
        (1, 2, 3, 4)),
        1234)

    # 1.7
    def test_pretty_multiplication_table(self):
        self.assertEqual(Tasks.pretty_multiplication_table(
        2,4,3,7), 
        [['', 3, 4, 5, 6, 7], 
        [2, 6, 8, 10, 12, 14], 
        [3, 9, 12, 15, 18, 21], 
        [4, 12, 16, 20, 24, 28]])

if __name__ == "__main__":
    unittest.main()
