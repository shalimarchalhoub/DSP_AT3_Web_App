import unittest
import pandas as pd

from src.serie_date.queries import *

#added library
import warnings
import psycopg2
from psycopg2 import OperationalError

username = 'postgres'
password = 'admin'
host = 'localhost'
port = '5432'
database = 'postgres'
schema_name = 'public'
table_name = 'mockcustomer'
col_name = 'cust_dob'

def test_connect():
    try:
        conn = psycopg2.connect(
            user = username,
            password = password,
            host = host,
            port = port,
            database = database
        )
    except (Exception, psycopg2.DatabaseError) as error:
        return False 
    return conn

conn = test_connect()

class TestDataDateQueries(unittest.TestCase):
    def setUp(self):
        '''
        this function's use is for ignoring this warning
        UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or 
        sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
        '''
        warnings.simplefilter('ignore', category=UserWarning)

    def test_dataDate_get_min_date_query(self):
        print("\n\n..[Testing get_min_date_query]..\n")
        sql_query = get_min_date_query(schema_name, table_name, col_name)
        print(sql_query,"\n\n")
        print("-->[after printing this sql_query, I copy the query and try it in pgAdmin to know whether this query run well]\n")
        result = pd.read_sql_query(sql_query,conn)
        print("-->[after executing with pandas to test how many rows returned]\n")
        self.assertEqual(len(result), 1)

    def test_dataDate_get_weekend_count_query(self):
        print("\n\n..[Testing get_weekend_count_query]..\n")
        sql_query = get_weekend_count_query(schema_name, table_name, col_name)
        print(sql_query,"\n\n")
        print("-->[after printing this sql_query, I copy the query and try it in pgAdmin to know whether this query run well]\n")
        result = pd.read_sql_query(sql_query,conn)
        print("-->[after executing with pandas to test how many rows returned]\n")
        self.assertEqual(len(result), 1)

    def test_dataDate_get_1900_count_query(self):
        print("\n\n..[Testing get_1900_count_query]..\n")
        sql_query = get_1900_count_query(schema_name, table_name, col_name)
        print(sql_query,"\n\n")
        print("-->[after printing this sql_query, I copy the query and try it in pgAdmin to know whether this query run well]\n")
        result = pd.read_sql_query(sql_query,conn)
        print("-->[after executing with pandas to test how many rows returned]\n")
        self.assertEqual(len(result),1 )


if __name__ == '__main__':
    unittest.main(verbosity=2)
