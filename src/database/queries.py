import pandas as pd
import psycopg2

def get_tables_list_query():
    """
        --------------------
        Description
        --------------------
        -> get_tables_list_query (method): Function that returns the query used for extracting the list of
        tables from a Postgres table

        --------------------
        Parameters
        --------------------
        ->This function takes zero parameters

        --------------------
        Pseudo-Code
        --------------------
        ->This code returns the query for extracting the list of tables from a Postgres table

        --------------------
        Returns
        --------------------
       ->return  type is string/two-dimensional tabular structure with labelled axes ,it returns the query for extracting the list of table from a Postgres table
        """

    conn = psycopg2.connect("dbname = mahjabeen  user = mahjabeen  password = 12345")

    query=("""SELECT table_name
             as table_name
             FROM   information_schema.tables
             WHERE table_schema != 'information_schema' AND
             table_schema != 'pg_catalog'""")

    df=pd.read_sql_query(query,conn)
    return(df)

def get_table_data_query(schema_name, table_name):
    """
        --------------------
        Description
        --------------------
        -> get_table_data_query (method): Function that returns the query used for extracting the content
        of a Postgres table

        --------------------
        Parameters
        --------------------
        ->schema_name, type is string, it takes the name of the schema from the user as one of the inputs
        -> table_name, type is string, it takes the name of the table as one of the inputs

        --------------------
        Pseudo-Code
        --------------------
        ->This code returns the query used for extracting the content of a Postgres table

        --------------------
        ->Returns: return type is
        --------------------
       ->return  type is string/two-dimensional tabular structure with labelled axes. It returns the query
       used for extracting the content of a Postgres table

        """

    conn = psycopg2.connect("dbname = mahjabeen  user = mahjabeen  password = 12345")
    query=("""select * from {0}.{1}""".format(schema_name,table_name))
    df=pd.read_sql_query(query,conn)
    print (df)
    return(df)

def get_table_schema_query(schema_name, table_name):
    """
        --------------------
        Description
        --------------------
        -> get_table_schema_query (method): Function that returns the query used for extracting the list of
        columns from a Postgres table and their information

        --------------------
        Parameters
        --------------------
         ->schema_name, type is string, it takes the name of the schema from the user as one of the inputs
        -> table_name, type is string, it takes the name of the table as one of the inputs

        --------------------
        Pseudo-Code
        --------------------
       ->This codes returns the query used for extracting the list of columns from a Postgres table and their information

        --------------------
        Returns
        --------------------
        ->return  type is string/two-dimensional tabular structure with labelled axes.It returns the query used for extracting the list of columns from a Postgres table and their information

        """
    conn = psycopg2.connect("dbname = mahjabeen  user = mahjabeen  password = 12345")
    query = ("""select c.table_name,c.column_name,c.data_type
           ,(case when k.COLUMN_NAME=c.column_name then c.column_name else '' end)  as primary_key
           , is_nullable,c.character_maximum_length,c.numeric_precision

    FROM
        information_schema.columns as c inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE as k  
        on c.table_name=k.table_name
        where c.table_name = '{1}' and c.table_schema='{0}'""".format(schema_name, table_name))
    df=pd.read_sql(query,conn)
    return df


get_table_schema_query('public','products')



