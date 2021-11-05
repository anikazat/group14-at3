# To be filled by students
import unittest 
from numpy import datetime64
import pandas as pd
import sys
sys.path.append("..")
from src.datetime import DateColumn

class DateColumn(unittest.TestCase):
    ###s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')###
    ### tried to create pd.series here, but it doesn't pass it to the test methods below###
    

    def test_get_name(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)
        

        #run method
        expected = s.name
        actual = self.get_name(s)

        #verify result
        self.assertEqual(expected, actual)


    def test_get_unique(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        #run method
        expected = 3
        actual = self.get_unique(s)

        #verify result
        self.assertEqual(expected, actual)

    def test_get_missing(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        #run method
        expected = 1
        actual = self.get_missing(s)

        #verify result
        self.assertEqual(expected, actual)

    def test_get_weekend(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        #run method
        expected = 0
        actual = self.get_weekend(s)

        #verify result
        self.assertEqual(expected, actual)

    def test_get_weekday(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        #run method
        expected = 4
        actual = self.get_weekday(s)

        #verify result
        self.assertEqual(expected, actual)


    def test_get_future(self):
        #create a pd.series (datetime type) with a future date 2023
        s = pd.Series(['2023-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)  

        #run method
        expected = 1
        actual = self.get.future(s)

        #verify result
        self.assertEqual(expected, actual)  

    def test_get_1900(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        #run method
        expected = 2
        actual = self.get_empty_1900(s)

        #verify result
        self.assertEqual(expected, actual)

    def test_get_1970(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        #run method
        expected = 0
        actual = self.get_empty_1970(s)

        #verify result
        self.assertEqual(expected, actual)


    def test_get_min(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        #run method
        expected = '1900-01-01 00:00:00'
        actual = self.get_min(s)

        #verify result
        self.assertEqual(expected, actual)

    def test_get_max(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        #run method
        expected = '2021-11-04 00:00:00'
        actual = self.get.max(s)

        #verify result
        self.assertEqual(expected, actual)
        

        
if __name__ == '__main__':
    unittest.main()        
