import unittest
import pandas as pd

from src.serie_date.logics import DateColumn
from src.database.logics import PostgresConnector

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

def test_connect_pg():
    warnings.simplefilter('ignore', category=UserWarning)
    db = PostgresConnector(database,username,password,host,port)
    db.open_connection()
    return db

db = test_connect_pg()

class TestSerieDateLogics(unittest.TestCase):

    def setUp(self):
        '''
        this function use for ignore this warning
        UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or 
        sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
        '''
        warnings.simplefilter('ignore', category=UserWarning)

    dateColumn = DateColumn(schema_name, table_name, col_name, db)

    def test_create_instance_dataColumn(self):
        print("\n..[Testing Create Instance of DateColumn]..")
        self.assertIsInstance(self.dateColumn,DateColumn)

    def test_datecolumn_is_serie_none(self):
        print("\n..[Testing Serie is None]..")
        self.assertFalse(self.dateColumn.is_serie_none())

    def test_datecolumn_set_unique(self):
        print("\n..[Testing Set Unique]..")
        self.dateColumn.set_unique()
        self.assertEqual(self.dateColumn.n_unique, 5)

    def test_datecolumn_set_missing(self):
        print("\n..[Testing Missing Data]..")
        self.dateColumn.set_missing()
        self.assertEqual(self.dateColumn.n_missing, 0)  

    def test_datecolumn_set_min(self):
        print("\n..[Testing compute minimum date in column]..")
        self.dateColumn.set_min()
        self.assertEqual(self.dateColumn.col_min.strftime('%Y-%m-%d'),'1900-10-09')  

    def test_datecolumn_set_max(self):
        print("\n..[Testing compute maximum date in column]..")
        self.dateColumn.set_max()
        self.assertEqual(self.dateColumn.col_max.strftime('%Y-%m-%d'),'1970-04-09')

    def test_datecolumn_set_weekend(self):
        print("\n..[Testing compute weekend days]..")
        self.dateColumn.set_weekend()
        self.assertEqual(self.dateColumn.n_weekend, 1)

    def test_datecolumn_set_weekday(self):
        print("\n..[Testing compute weekday days]..")
        self.dateColumn.set_weekday()
        self.assertEqual(self.dateColumn.n_weekday, 5)

    def test_datecolumn_set_future(self):
        print("\n..[Testing compute future days]..")
        self.dateColumn.set_future()
        self.assertEqual(self.dateColumn.n_future, 0)

    def test_datecolumn_set_empty_1900(self):
        print("\n..[Testing compute how many date that in 1990]..")
        self.dateColumn.set_empty_1900()
        self.assertEqual(self.dateColumn.n_empty_1900, 0)

    def test_datecolumn_set_empty_1970(self):
        print("\n..[Testing compute how many date that in 1970]..")
        self.dateColumn.set_empty_1970()
        self.assertEqual(self.dateColumn.n_empty_1970, 0)

    def test_datecolumn_set_data(self):
        print("\n..[Testing Set Data for date column]..")
        self.dateColumn.set_data()
        #after computing every summary needed in set data, then we test each value
        self.assertEqual(self.dateColumn.n_unique, 5)
        self.assertEqual(self.dateColumn.n_missing, 0)
        self.assertEqual(self.dateColumn.col_min.strftime('%Y-%m-%d'), '1900-10-09')
        self.assertEqual(self.dateColumn.col_max.strftime('%Y-%m-%d'), '1970-04-09')  
        self.assertEqual(self.dateColumn.n_weekend,1)
        self.assertEqual(self.dateColumn.n_weekday,5)
        self.assertEqual(self.dateColumn.n_future,0)
        self.assertEqual(self.dateColumn.n_empty_1900,0)
        self.assertEqual(self.dateColumn.n_empty_1970,0)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
