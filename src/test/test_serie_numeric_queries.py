import unittest
import pandas as pd

from src.serie_numeric.queries import *

class TestSerieNumericQueries(unittest.TestCase):
    def test_negative_number_queries(self):
        sql = get_negative_number_query('test_schema', 'test_table', 'test_column')
        self.assertEqual('select count(test_column) from test_schema.test_table where test_column < 0', sql)
    
    def test_unique_query(self):
        sql = get_unique_query('test_schema', 'test_table', 'test_column')
        self.assertEqual('select distinct test_column from test_schema.test_table', sql)
        
    def test_std_query(self):
        sql = get_std_query('test_schema', 'test_table', 'test_column')
        self.assertEqual('select std(test_column) from test_schema.test_table', sql)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)