import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import sys
import psycopg2
from psycopg2 import OperationalError
from src.database.logics import PostgresConnector


class PostgresConnectorTestCace(unittest.TestCase):
    global con
    con = psycopg2.connect("dbname=mahjabeen user=mahjabeen password=12345")
    def test_Constructor(self):

        global constructor
        constructor=PostgresConnector('mahjabeen','mahjabeen','12345','localhost','5432')
        self.assertEqual(constructor.user,'mahjabeen')
        self.assertEqual(constructor.password, '12345')
        self.assertEqual(constructor.host, 'localhost')
        self.assertEqual(constructor.port, '5432')

    def test_open_connection(self):
        constructor.open_connection()
        self.assertEqual(constructor.conn.status,psycopg2.extensions.STATUS_READY)

    def test_close_connection(self):

        self.assertNotEqual(constructor.close_connection(),psycopg2.extensions.STATUS_READY)

    def test_open_cursor(self):
        constructor.open_cursor()
        constructor.cur.execute("select * from products")

        self.assertEqual(constructor.conn.status,psycopg2.extensions.STATUS_BEGIN)

    def test_close_cursor(self):
        self.assertEqual(constructor.close_cursor(),None)

    def test_run_query(self):
        result1=constructor.run_query("select * from public.products")
        query=("select * from public.products")
        df1=pd.read_sql(query,con)
        assert_frame_equal(result1,df1)

    def test_list_tables(self):
        result1=constructor.list_tables()
        #con=psycopg2.connect("dbname=mahjabeen user=mahjabeen password=12345")
        query=("""SELECT table_name
             as table_name
             FROM   information_schema.tables
             WHERE table_schema != 'information_schema' AND
             table_schema != 'pg_catalog'""")
        result2=pd.read_sql_query(query,con)
        assert_frame_equal(result1,result2)

    def test_load_table(self):
        result1=constructor.load_table('public','suppliers')
        query=("""select * from suppliers""")
        result2=pd.read_sql_query(query,con)
        assert_frame_equal(result1,result2)
    def test_get_table_schema(self):
        result1=constructor.get_table_schema('public', 'suppliers')
        query = ("""select c.table_name,c.column_name,c.data_type
                  ,(case when k.COLUMN_NAME=c.column_name then c.column_name else '' end)  as primary_key
                  , is_nullable,c.character_maximum_length,c.numeric_precision

           FROM
               information_schema.columns as c inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE as k  
               on c.table_name=k.table_name
               where c.table_name = 'suppliers' and c.table_schema='public'""")
        result2=pd.read_sql_query(query,con)
        assert_frame_equal(result1, result2)



if __name__ == '__main__':
    unittest.main(verbosity=2)