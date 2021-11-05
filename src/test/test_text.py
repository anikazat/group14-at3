import unittest
import numpy as np
import pandas as pd
sys.path.append("..")
import sys
from src.text import TextColumn



class TestColumn(unittest.TestCase):
    test_data = pd.DataFrame({'test':np.random.choice(50)})
    for column_name in test_data.columns:
        test_text=TextColumn(column_name,pd.Series(test_data[column_name]))
        
        test_value=test_data[f"{column_name}"]

    def test_get_name(self):
        text_name=self.test_text.get_name()

        self.assertEqual(text_name, self.column_name)

    def test_get_unique(self):
        text_unique=self.test_text.get_unique()
        test_unique=len(self.test_value.unique())

        self.assertEqual(text_unique, len(test_unique))

    def test_get_missing(self):
        test_missing=self.test_value.isnull().sum()

        self.assertEqual(self.test_text.get_missing(), test_missing)


    def test_get_empty(self):
        test_empty=(self.test_value == '').sum()

        self.assertEqual(self.test_text.get_zeros(), test_empty)

    def test_get_whitespace(self):
        test_whitespace=(self.test_value == ' ').sum()

        self.assertEqual(self.test_text.get_whitespace(), test_whitespace)

    def test_get_lowercase(self):
        test_lowercase=self.test_value.str.count(str.islower == True)

        self.assertEqual(self.test_text.get_lowercase(), test_lowercase)

    def test_get_uppercase(self):
        test_uppercase=self.test_value.str.count(str.isupper == True)

        self.assertEqual(self.test_text.get_uppercase(), test_uppercase)

    def test_get_alphabet(self):
        test_alphabet = self.test_value.count(str.isalpha == True)

        self.assertEqual(self.test_text.get_alphabet, test_alphabet)

    def test_get_digit(self):
        test_digit = self.test_value.count(str.isnumeric == True)

        self.assertEqual(self.test_text.get_digit, test_digit)

    def test_get_mode(self):
        test_mode = self.test_value.mode()

        self.assertEqual(self.test_text.get_mode(), test_mode)

    def test_get_barchart(self):
        test_barchart = self.test_value.value_counts()

        self.assertEqual(self.test_text.get_barchart(), test_barchart)

    def test_frequent(self):
        text_DataFrame=type(self.test_text.frequent())
        
        self.assertEqual(text_DataFrame, type(self.test_data))

    def test_data(self):
        text_table = type(self.test_text.table())
        
        self.assertEqual(text_table, type(self.test_data))


if __name__ == '__main__':
    unittest.main()


