import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import psycopg2
from src.database.queries import *

global conn
conn=psycopg2.connect("dbname=mahjabeen user=mahjabeen password=12345")
def test_get_tables_list_query():
    query1=get_tables_list_query()
    result1=pd.read_sql_query(query1,conn)
    query2=("""select table_name as table_name
                 from   information_schema.tables
                 where table_schema != 'information_schema' and
                 table_schema != 'pg_catalog'""")
    result2 = pd.read_sql_query(query2, conn)
    assert_frame_equal(result1,result2)

def test_get_table_data_query():
    query1=get_table_data_query('public','products')
    result1=pd.read_sql_query(query1,conn)
    query2 = ("""select * from public.products""")
    result2=pd.read_sql_query(query2,conn)
    assert_frame_equal(result1,result2)
def test_get_table_schema_query():
    query1=get_table_schema_query('public','products')
    result1=pd.read_sql_query(query1,conn)
    query2=("""select c.table_name,c.column_name
          ,c.data_type,(case when k.COLUMN_NAME=c.column_name then c.column_name else '' end)  as primary_key
          , is_nullable,c.character_maximum_length,c.numeric_precision
            FROM
	        information_schema.columns as c inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE as k  
	        on c.table_name=k.table_name
	        where c.table_name = 'products' and c.table_schema='public'""")
    result2=pd.read_sql_query(query2,conn)
    assert_frame_equal(result1,result2)

if __name__ == '__main__':
    unittest.main(verbosity=2)