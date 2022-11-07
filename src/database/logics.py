import psycopg2
from psycopg2 import OperationalError
import pandas as pd
import sys
sys.path.insert(0,'/home/mahjabeen/src/database')
from queries import get_tables_list_query, get_table_data_query, get_table_schema_query


class PostgresConnector:
    """
    --------------------
    Description
    --------------------
    -> PostgresConnector (class): Class that manages the connection to a Postgres database

    --------------------
    Attributes
    --------------------
    -> database (str): Name of Postgres database (mandatory)
    -> user (str): Username used for connecting to Postgres database (mandatory)
    -> password (str): Password used for connecting to Postgres database (mandatory)
    -> host (str): URL of Postgres database (mandatory)
    -> port (str): Port number of Postgres database (mandatory)
    -> conn (psycopg2._psycopg.connection): Postgres connection object (optional)
    -> cursor (psycopg2._psycopg.connection.cursor): Postgres cursor for executing query (optional)
    -> excluded_schemas (list): List containing the names of internal Postgres schemas to be excluded from selection (information_schema, pg_catalog)
    """

    def __init__(self, database,user,password,host='127.0.0.1',port='5432'):

        self.database=database
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        self.conn=None
        self.cur=None

    def open_connection(self):
        """
            --------------------
            Description
            --------------------
            -> open_connection (method): Class method that creates an active connection to a Postgres database

            --------------------
           Parameters:
           ->self: PostgresConnector object, with reference to it, the user can access any parameter
           of the PostgresConnector class
           ->database: str, it holds the database name
           ->user:str, it holds the username of the postgres user
           ->password:str, it holds the password of the user to connect to the postgres databse
           ->host:str, it holds the hostname/address of the postgress server
           ->conn:str, it holds the connection information to the postgres server
           ->cur:str, it holds the information of cursor open so that the user can initiate
            a transaction to the database
            --------------------
            Pseudo-Code
            --------------------
            -> pseudo-code: This code helps the user to connect to the databse

            --------------------
            ->Returns: type is str, It returns the connection information and up on successful it tells the user that
            it is connected to the databse or tells the user that the connection was unsuccessful
            --------------------
        """
        try:

             self.conn=psycopg2.connect("dbname={0} user={1}  password={2}".format(self.database, self.user, self.password))

             return(self.conn)




        except (Exception, psycopg2.DatabaseError) as error:
             print(error)
    def close_connection(self):
        """
        --------------------
        Description
        --------------------
        -> close_connection (method): Class method that closes an active connection to a Postgres database

        --------------------
        Parameters
        --------------------
       ->self: PostgresConnector object, with reference to it, the user can access any parameter
       of the PostgresConnector class
        --------------------
        ->Pseudo-Code: This code helps the user to close an active connection to a Postgres databse
        --------------------
       ->Returns:type is str, It will tell the user that the connection is whether closed or not to the Postgres database
        --------------------
        """

        if self.conn is not None:
           self.conn.close()
           print('Database Connection is closed now')
        else:
            print("connection is still active")

    def open_cursor(self):
        """
        --------------------
        Description
        --------------------
        -> open_cursor (method): Class method that creates an active cursor to a Postgres database

        --------------------
        Parameters:

        --------------------
        -->self: PostgresConnector object, with reference to it, the user can access any parameter
        of the PostgresConnector class

        --------------------
        Pseudo-Code
        --------------------
        -> This code opens the cursor for the user to initiate a transaction from or to the Postgres databse

        --------------------
        Returns
        --------------------
        ->type is str, It returns the ability to the  user to pull or load information from or into the Postgres database

        """
        self.open_connection()
        self.cur = self.conn.cursor()
        if self.cur is not None:
            print("Cursor is opened")


        else:
            print("Cursor is already closed")

    def close_cursor(self):
            """
            --------------------
            Description
            --------------------
            -> close_cursor (method): Class method that closes an active cursor to a Postgres database

            --------------------
            Parameters
            --------------------
            -->self: PostgresConnector object, with reference to it, the user can access any parameter
            of the PostgresConnector class

            --------------------
            Pseudo-Code
            --------------------
            ->This code closes the cursor to the Postgres database

            --------------------
            Returns
            --------------------
            -> type is str, It returns the curser closed message and if the user try to pull or load the information to the
            database, it throws an error
            """
            self.open_cursor()
            self.cur=self.cur.close()
            print(self.cur)

            if self.cur is None:
                print("cursor is closed now")
            else:
                print("Cursor is still opened")

    def run_query(self, sql_query):
        """
        --------------------
        Description
        --------------------
        -> run_query (method): Class method that executes a SQL query and returns the result as a
        Pandas dataframe

        --------------------
        Parameters
        --------------------
        ->self:PostgresConnector object, with reference to it, the user can access any parameter
            of the PostgresConnector class
        ->sql_query: str, it takes the sql_query as an input from the user

        --------------------
        Pseudo-Code
        --------------------
       ->This code takes the input as query from the user and depending upon the requirements,
         it fetch or load the information into or from the Postgres database

        --------------------
        Returns
        --------------------
        ->return type is string/two-dimensional tabular structure with labelled axes(rows and columns), it returns the result of the query
        """
        self.open_connection()
        df=pd.read_sql(sql_query,self.conn)
        print(df)
        return df


    def list_tables(self):
        """
        --------------------
        Description
        --------------------
        -> list_tables (method): Class method that extracts the list of available tables using a SQL
        query (get_tables_list_query())

        --------------------
        Parameters
        --------------------
        ->self:PostgresConnector object, with reference to it, the user can access any parameter
        of the PostgresConnector class
        --------------------
        Pseudo-Code
        --------------------
        ->This code helps the user to call the method, get_tables_list_query() to extracts the list of
        available tables

        --------------------
        Returns
        --------------------
        ->return type is string/two-dimensional tabular structure with labelled axes(rows and columns), it returns the list of available tables(dataframe)

        """
        query=get_tables_list_query()
        df=pd.read_sql_query(query,self.conn)
        print(df)
        return df

    def load_table(self, schema_name, table_name):
        """
        --------------------
        Description
        --------------------
        -> load_table (method): Class method that load the content of a table using a SQL query (get_table_data_query())

        --------------------
        Parameters
        --------------------
        ->self:PostgresConnector object, with reference to it, the user can access any parameter
       of the PostgresConnector class
        ->schema_name, type is string, it takes the name of the schema from the user as one of the inputs
        -> table_name, type is string, it takes the name of the table as one of the inputs
        --------------------
        Pseudo-Code
        --------------------
        This code helps the user to load the content of a table by calling get_table_data_query() method.
        --------------------
        Returns
        --------------------
        ->return  type is string/two-dimensional tabular structure with labelled axes(rows and columns), It returns the content(dataframe) of a table
        """

        query=get_table_data_query(schema_name,table_name)
        df=pd.read_sql_query(query,self.conn)
        print(df)
        return(df)


    def get_table_schema(self, schema_name, table_name):

        """
         --------------------
         Description
         --------------------
         -> get_table_schema (method): Class method that extracts the schema information of a table
         using a SQL query (get_table_schema_query())

         --------------------
         Parameters
         --------------------
         ->self:PostgresConnector object, with reference to it, the user can access any parameter
         of the PostgresConnector class
         ->schema_name, type is string, it takes the name of the schema from the user as one of the inputs
         -> table_name, type is string, it takes the name of the table as

         --------------------
         Pseudo-Code
         --------------------
         -> This code helps the user to extracts the schema information of a table by calling
         get_table_schema_query(schema_name,table_name)

         --------------------
         Returns
         --------------------
         -> ->return  type is string/two-dimensional tabular structure with labelled axes(rows and columns),
         It returns the schema information(dataframe) of a table.
        """
        query=get_table_schema_query(schema_name, table_name)
        df=pd.read_sql_query(query,self.conn)
        print(df)
        return df

"""
pconnector=PostgresConnector('mahjabeen','mahjabeen','12345','localhost','5432')

pconnector.run_query("select * from suppliers")
pconnector.list_tables()
pconnector.load_table('public','employees')
pconnector.get_table_schema('public','products')



pconnector=PostgresConnector('{}'.format(database),'{}'.format(user),'{}'.format(database))
pconnector.run_query("select * from suppliers")
pconnector.list_tables()
pconnector.load_table('public','employees')
pconnector.get_table_schema('public','products')
print("list table starts")


database,user,password=input("enter dbname,username,password seperated a space,").split()
pconnector=PostgresConnector('{}'.format(database),'{}'.format(user),'{}'.format(database))

pconnector.run_query("select * from suppliers")
pconnector.list_tables()
pconnector.load_table('public','employees')
pconnector.get_table_schema('public','products')


print('{}'.format(database),'{}'.format(user),'{}'.format(database))

schema_name,table_name=input("Now enter the schema_name and table_name seperated by a space").split()
pconnector.run_query("select * from {0}.{1}".format(schema_name,table_name))
pconnector.list_tables()
pconnector.load_table('{0}','{1}'.format(schema_name,table_name))
pconnector.get_table_schema('{0}','{1}'.format(schema_name,table_name))

"""












