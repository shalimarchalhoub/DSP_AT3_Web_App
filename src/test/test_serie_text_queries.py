import unittest
import pandas as pd
import numpy as np

import sys
sys.path.append('../')
from src.serie_text.logics import TextColumn


class TestIsSeriesNone(unittest.TestCase):
    def test_is_serie_none(self):
        datanone = []
        data =['apple' , 'kiwi', 'mango'] 
        self.assertEqual(datanone.is_serie_none(), True)
        self.assertEqual(data.is_serie_none(), False)

class Test_Text_Unique(unittest.TestCase):
    def test_name1(self):

        test = TextColumn()
        test2 = TextColumn()
        test3 = TextColumn()
        test4 = TextColumn()

        test.serie = {'test': ['A','B','C', 'D', 'AB', 'AB', 'V']}
        test2.serie = {'test': ['A','B','C',25,25,3]}
        test3.serie = {'test': ['A','B','$', '*', '&', '$', '#']}
        test4.serie = {'test':['A', 'B' , 'C' , 'C', 12, 3 , 12, '*', '*', '#']}

        result = test.set_unique()
        result2 = test2.set_unique()
        result3 = test3.set_unique()
        result4 = test4.set_unique()

        self.assertEqual(result, 5)
        self.assertEqual(result2, 4)
        self.assertEqual(result3, 4)
        self.assertEqual(result4, 4)


class Test_Missing(unittest.TestCase):
    def test_missing_value(self):

        test1 = TextColumn()
        test2 = TextColumn()

        test1.serie = ['A','B','C','D',np.NaN, 'F', np.NaN]
        test2.serie = ['A', 'B','C', 1, 2, '']

        result1 = test1.set_missing()
        result2 = test2.set_missing()

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 0)


class Test_Empty(unittest.TestCase):
    def test_empty_value(self):

        test1 = TextColumn()
        test2 = TextColumn()

        test1.serie = ['A','B','C','D',' ',' ' 'F', np.NaN, 'G']
        test2.serie = ['A', 'B','C', 1, 2]

        result1 = test1.set_empty()
        result2 = test2.set_empty()

        self.assertEqual(result1, 2)
        self.assertEqual(result2, 0)


class Test_Mode(unittest.TestCase):
    def test_mode_value(self):

        test1 = TextColumn()
        test2 = TextColumn()

        test1.serie = ['A','A','A','A',' ',' ' 'F', np.NaN, 'G']
        test2.serie = [1, 1,'C', 1, 2]

        result1 = test1.set_mode()
        result2 = test2.set_mode()

        self.assertEqual(result1, 'A')
        self.assertEqual(result2, 1)

class Test_Text_Whitespace(unittest.TestCase):
    def test_value_whitespace(self):
        
        test1 = TextColumn()
        test2 = TextColumn()

        test1.serie = [' ','    ','A','A','',' ' 'F', np.NaN, 'G']
        test2.serie = [1, 1,'C', 1, 2]

        result1 = test1.set_whitespace()
        result2 = test2.set_whitespace()

        self.assertEqual(result1, 4)
        self.assertEqual(result2, 0)


class Test_Lower_Case(unittest.TestCase):
    def test_value_Lowercase(self):
        
        test1 = TextColumn()
        test2 = TextColumn()

        test1.serie = ['Apple','apple','Ab','a','c','juicE', np.NaN, 'G']
        test2.serie = [1, 1,'C', 1, 2]

        result1 = test1.set_lowercase()
        result2 = test2.set_lowercase()

        self.assertEqual(result1, 3)
        self.assertEqual(result2, 0)


class Test_Upper_Case(unittest.TestCase):
    def test_value_uppercase(self):
        
        test1 = TextColumn()
        test2 = TextColumn()

        test1.serie = ['APPLE','Apple','apple','A','ABC','JuicE', np.NaN, ' ']
        test2.serie = [1, '%','C', '', 'a', 1, 2]

        result1 = test1.set_uppercase()
        result2 = test2.set_uppercase()

        self.assertEqual(result1, 3)
        self.assertEqual(result2, 1)

class Test_Alphabet(unittest.TestCase):
    def test_value_alphabet(self):
        
        test1 = TextColumn()
        test2 = TextColumn()

        test1.serie = ['APPLE','Apple12','12apple',12,'A','AB11C','JuicE', np.NaN, '&%']
        test2.serie = [1, '%','C', '', 'a', 1, 2]

        result1 = test1.set_alphabet()
        result2 = test2.set_alphabet()

        self.assertEqual(result1, 3)
        self.assertEqual(result2, 2)

class Test_Digit(unittest.TestCase):
    def test_value_digit(self):
        
        test1 = TextColumn()
        test2 = TextColumn()

        test1.serie = ['APPLE','Apple12','12apple', 12,'A','AB11C','JuicE', np.NaN, '&%']
        test2.serie = [1232, '%','C', '', 'a', 1111, 233, 1, 12, 0.9]

        result1 = test1.set_alphabet()
        result2 = test2.set_alphabet()

        self.assertEqual(result1, 1)
        self.assertEqual(result2, 6)

class Test_Text_bar(unittest.TestCase):
    def test_bar_chart(self):
        test = TextColumn()
        test.serie = ['A','B','cd', 'efg', 'h']

        class_str = str(type(test.get_barchart()))
        chart_class = class_str.split('"')
        chart_str = chart_class[0]
        self.assertEqual(chart_str, "<class 'altair.vegalite.v4.api.Chart'>")


class Test_Text_frequent(unittest.TestCase):
    def test_frequest(self):    
        test = TextColumn()
        test.serie = ['A','B','cd', 'efg', 'h']
        
        class_str = str(type(test.get_frequent()))
        table_class = class_str.split('"')
        chart_str = table_class[0]
        self.assertEqual(chart_str, "<class 'pandas.core.frame.DataFrame'>")


if __name__ == '__main__':
    unittest.main(verbosity=2)
