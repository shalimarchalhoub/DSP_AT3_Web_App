import unittest
import pandas as pd

from src.serie_text.queries import *

class TestGetMissingQuery(unittest.TestCase):
    def test_get_missing_query(self):
        schema_name = "public"
        table_name = "supplier"
        col_name = "column"
        query = ' '.join(get_missing_query(schema_name,table_name,col_name).split())
        self.assertEqual(query,' '.join("""
        
        SELECT COUNT(test_col) 
        FROM public.test_table 
        WHERE test_col IS NULL;
        """.split()))

class TestGetModeQuery(unittest.TestCase):
    def test_get_mode_query(self):
        schema_name = "public"
        table_name = "supplier"
        col_name = "column"
        query = ' '.join(get_mode_query(schema_name,table_name,col_name).split())
        self.assertEqual(query, ' '.join("""

        SELECT MODE()
        WITHIN GROUP(ORDER BY test_col) AS mode
        FROM public.test_table;
        
        """.split()))

class TestGetAlphaQuery(unittest.TestCase):
    def test_get_alpha_query(self):
        schema_name = "public"
        table_name = "supplier"
        col_name = "column"
        query = ' '.join(get_alpha_query(schema_name, table_name, col_name).split())
        self.assertEqual(query, ' '.join("""
        
        SELECT COUNT(test_col) 
        FROM public.test_table
        WHERE test_col LIKE '%[a-zA-Z]%';
        
        
        
        """.split()))


if __name__ == '__main__':
    unittest.main(verbosity=2)
