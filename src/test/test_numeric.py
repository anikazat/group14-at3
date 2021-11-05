import numpy as np
import pandas as pd
import sys
sys.path.append("..")
from src.numeric import NumericColumn
import matplotlib.pyplot as plt


class TestNumeric(unittest.TestCase):
    test_data = pd.DataFrame({'test':np.random.randn(20)})
    for column_name in test_data.columns:
        test_numeric=NumericColumn(column_name,pd.Series(test_data[column_name]))
        test_value=test_data[f"{column_name}"]

    def test_get_name(self):
        numeric_name=self.test_numeric.get_name()
        self.assertEqual(numeric_name, self.column_name)

    def test_get_unique(self):
        numeric_unique=self.test_numeric.get_unique()
        test_unique=self.test_value.value_counts().sum()
        self.assertEqual(numeric_unique, test_unique)

    def test_get_missing(self):
        test_missing=self.test_value.isnull().sum()
        self.assertEqual(self.test_numeric.get_missing(), test_missing)


    def test_get_zeros(self):
        test_zeros=(self.test_value.values== 0).sum()
        self.assertEqual(self.test_numeric.get_zeros(), test_zeros)

    def test_get_negatives(self):
        test_negatives=(self.test_value.values< 0).sum()
        self.assertEqual(self.test_numeric.get_negatives(), test_negatives)

    def test_get_mean(self):
        test_mean=self.test_value.mean()
        self.assertEqual(self.test_numeric.get_mean(), test_mean)

    def test_get_std(self):
        test_std=self.test_value.std()
        self.assertEqual(self.test_numeric.get_std(), test_std)

    def test_get_min(self):
        test_min = self.test_value.min()
        self.assertEqual(self.test_numeric.get_min(), test_min)

    def test_get_max(self):
        test_max = self.test_value.max()
        self.assertEqual(self.test_numeric.get_max(), test_max)

    def test_get_median(self):
        test_median = self.test_value.median()
        self.assertEqual(self.test_numeric.get_median(), test_median)

    def test_get_histogram(self):
        fig, ax = plt.subplots()
        ax.hist(self.test_value, bins=50, edgecolor='white')
        #test the output is histogram
        self.assertEqual(type(self.test_numeric.get_histogram()), type(fig))

    def test_frequent(self):
        numeric_DataFrame=type(self.test_numeric.frequent())
        #test the output is DataFrame
        self.assertEqual(numeric_DataFrame, type(self.test_data))

    def test_table(self):
        numeric_table = type(self.test_numeric.table())
        # test the output is DataFrame
        self.assertEqual(numeric_table, type(self.test_data))


if __name__ == '__main__':
    unittest.main()

