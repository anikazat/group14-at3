import unittest
import pandas as pd
import numpy as np
import sys
sys.path.append('./')
from src.data import Dataset
import pandas.testing as pd_testing


class TestDataset(unittest.TestCase):

    ### Should this be here or inside each of the test functions? ###
    test_name = 'name.csv'
    test_df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
    test_data = Dataset(test_name, test_df)

    def test_get_name(self):
        # Run function
        test_result = self.test_data.get_name()
        
        # Verify results
        self.assertEqual(test_result, self.test_name) #or 'name.csv'
    
    def test_get_n_rows(self):
        # Run function
        test_result = self.test_data.get_n_rows()

        # Verify results
        self.assertEqual(test_result, len(self.test_df))

    def test_get_n_cols(self):
        # Run function
        test_result = self.test_data.get_n_cols()

        # Verify results
        self.assertEqual(test_result, len(self.test_df.columns))

    def test_get_cols_list(self):
        # Run function
        test_result = self.test_data.get_cols_list()

        # Verify results
        self.assertEqual(test_result, list(self.test_df.keys()))

    def test_get_cols_dtype(self):
        # Run function
        test_result = self.test_data.get_cols_dtype()

        # Verify results
        self.assertEqual(test_result, self.test_df.dtypes.apply(lambda x: x.name).to_dict())

    def test_get_n_duplicates(self):
        # Run function
        test_result = self.test_data.get_n_duplicates()

        # Verify results
        self.assertEqual(test_result, self.test_df.duplicated().sum())

    def test_get_n_missing(self):
        # Run function
        test_result = self.test_data.get_n_missing()

        # Verify results
        self.assertEqual(test_result, self.test_df.isna().count()[1])

    def test_get_head(self):
        # Run function
        test_result = self.test_data.get_head()

        # Verify results
        pd_testing.assert_frame_equal(test_result, self.test_df.head())
    
    def test_get_tail(self):
        # Run function
        test_result = self.test_data.get_tail()

        # Verify results
        pd_testing.assert_frame_equal(test_result, self.test_df.tail())

    # def test_get_sample(self):
    #     # Set up data to test
    #     # self.test_df.sample(n=5, random_state=1)
    #     # Run function
    #     test_result = self.test_data.get_sample()

    #     # Verify results
    #     self.assertEqual(test_result, pd.DataFrame)
    #     # pd_testing.assert_frame_equal(test_result, self.test_df.sample(5))
    
    def test_get_numeric_columns(self):
        # Run function
        test_result = self.test_data.get_numeric_columns()

        # Verify results
        self.assertEqual(test_result, list(self.test_df.select_dtypes(include=['int64','float64']).columns))

    def test_get_text_columns(self):
        # Run function
        test_result = self.test_data.get_text_columns()

        # Verify results
        self.assertEqual(test_result, list(self.test_df.select_dtypes(include=['O']).columns))

    def test_get_date_columns(self):
        # Run function
        test_result = self.test_data.get_date_columns()

        # Verify results
        self.assertEqual(test_result, list(self.test_df.select_dtypes(include=['datetime64[ns]']).columns))
        
                

if __name__ == '__main__':
    unittest.main()