# To be filled by students
import unittest 
from src.datetime import DateColumn
from numpy import datetime64
import pandas as pd



class DateColumn(unittest.TestCase):
    ###s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')###
    ### tried to create pd.series here, but it doesn't pass it to the test methods below###
    

    def test_get_name(self):
        #create a pd.series (datetime type)
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = s.name
        actual = self.get_name(s)

        #verify result
        self.assertEqual(expected, actual)


    def test_get_unique(self):
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = 3
        actual = self.get_unique(s)
        self.assertEqual(expected, actual)

    def test_get_missing(self):
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = 1
        actual = self.get_missing(s)
        self.assertEqual(expected, actual)

    def test_get_weekend(self):
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = 0
        actual = self.get_weekend(s)
        self.assertEqual(expected, actual)

    def test_get_weekday(self):
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = 4
        actual = self.get_weekday(s)
        self.assertEqual(expected, actual)


    def test_get_future(self):
        s = pd.Series(['2023-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)  

        expected = 1
        actual = self.get.future(s)
        self.assertEqual(expected, actual)  

    def test_get_1900(self):
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = 2
        actual = self.get_empty_1900(s)
        self.assertEqual(expected, actual)

    def test_get_1970(self):
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = 0
        actual = self.get_empty_1970(s)
        self.assertEqual(expected, actual)


    def test_get_min(self):
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = '1900-01-01 00:00:00'
        actual = self.get_min(s)
        self.assertEqual(expected, actual)

    def test_get_max(self):
        s = pd.Series(['2021-11-04', '2014-05-05', '','1900-01-01','1900-01-01'], name='Datetime')
        s= pd.to_datetime(s)

        expected = '2021-11-04 00:00:00'
        actual = self.get.max(s)
        self.assertEqual(expected, actual)

        

       
