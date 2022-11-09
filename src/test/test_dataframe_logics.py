import unittest
import pandas as pd

from src.dataframe.logics import Dataset
from src.database.logics import PostgresConnector

import warnings

username = 'postgres'
password = 'admin'
host = 'localhost'
port = '5432'
database = 'postgres'
schema_name = 'public'
table_name = 'mockcustomer'
db = None

def test_connect():
    db = PostgresConnector(database,username,password,host,port)
    db.open_connection()
    return db

def test_prepare_mock(db):
    commands = (
    """
    CREATE TABLE IF NOT EXISTS mockcustomer (
        cust_id INTEGER,
        cust_name VARCHAR(50) NOT NULL,
        cust_city VARCHAR(50),
        cust_dob date,
        cust_join_date date,
        limit_lending real
    )
    """,
    """
    delete from mockcustomer
    """,
    """
    insert into mockcustomer values('101','Michelle','Melbourne','1900-10-9','1930-05-1',2000)
    """,
    """ 
    insert into mockcustomer values('102','Michael','Sydney','1960-02-4','1970-06-03',3000)
    """,
    """ 
    insert into mockcustomer values('103','Liany','Sydney','1970-04-9','2000-05-03',null)
    """,
    """ 
    insert into mockcustomer values('104','Phoebe','Brisbane','1970-02-4','2000-06-10',3000)
    """,
    """ 
    insert into mockcustomer values('105','Jacinda','Perth','1960-03-12','2000-06-12',3000)
    """,
    """
    insert into mockcustomer values('101','Michelle','Melbourne','1900-10-9','1930-05-1',2000)
    """)    
    warnings.simplefilter('ignore', category=UserWarning)
    db.open_cursor()
    cur=db.cur
    for command in commands:
        cur.execute(command)
    cur.close()
    db.conn.commit()
    print("...........finish create mock customer")
    
db = test_connect()
test_prepare_mock(db)

class TestDataFrameLogics(unittest.TestCase):
    
    def setUp(self):
        '''
        this function use for ignore this warning
        UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or 
        sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
        '''
        warnings.simplefilter('ignore', category=UserWarning)

    dataset = Dataset(schema_name, table_name, db)

    def test_create_instance_dataset(self):
        print("\n..[Testing Create Instance]..")
        self.assertIsInstance(self.dataset,Dataset)

    def test_is_df_none(self):
        print("\n..[Test Data frame is None]..")
        self.assertFalse(self.dataset.is_df_none())

    def test_set_dimensions(self):
        print("\n..[Testing Dimension]..")
        self.dataset.set_dimensions()
        self.assertEqual(self.dataset.n_rows, 6)
        self.assertEqual(self.dataset.n_cols, 6)

    def test_set_duplicates(self):
        print("\n..[Testing duplicate]..")
        self.dataset.set_duplicates()
        self.assertEqual(self.dataset.n_duplicates, 1)

    def test_set_missing(self):
        print("\n..[Testing missing]..")
        self.dataset.set_missing()
        self.assertEqual(self.dataset.n_missing, 1)  

    def test_set_numeric_columns(self):
        print("\n..[Testing numeric column]..")
        self.dataset.set_numeric_columns()
        self.assertEqual(self.dataset.num_cols,['cust_id', 'limit_lending'])  

    def test_set_text_columns(self):
        print("\n..[Testing text column]..")
        self.dataset.set_text_columns()
        self.assertEqual(self.dataset.text_cols, ['cust_name', 'cust_city']) 

    def test_set_date_columns(self):
        print("\n..[Testing date column]..")
        self.dataset.set_date_columns()
        self.assertEqual(self.dataset.date_cols, ['cust_dob', 'cust_join_date'])

    def test_dataset_set_data(self):
        print("\n..[Testing Set Data]..")
        self.dataset.set_data()
        self.assertEqual(self.dataset.n_rows, 6)
        self.assertEqual(self.dataset.n_cols, 6)
        self.assertEqual(self.dataset.n_duplicates, 1)
        self.assertEqual(self.dataset.n_missing, 1)        
        self.assertEqual(self.dataset.num_cols,  ['cust_id', 'limit_lending'])
        self.assertEqual(self.dataset.text_cols, ['cust_name', 'cust_city'])
        self.assertEqual(self.dataset.date_cols, ['cust_dob', 'cust_join_date'])
        
    def test_dataset_get_data_head(self):
        print("\n..[Testing Head]..")
        self.assertEqual(self.dataset.df.iloc[0:1,0:1].values.tolist()[0][0], self.dataset.get_head(1).values.tolist()[0][0])
        
    def test_dataset_get_data_tail(self):
        print("\n..[Testing Tail]..")
        lendf = len(self.dataset.df) 
        self.assertEqual(self.dataset.df.iloc[lendf-1:lendf,0:1].values.tolist()[0][0], self.dataset.get_tail(1).values.tolist()[0][0])

if __name__ == '__main__':
    unittest.main(verbosity=2)
