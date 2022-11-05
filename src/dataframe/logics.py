import pandas as pd
import streamlit as st

from src.database.logics import PostgresConnector
from src.dataframe.queries import get_numeric_tables_query, get_text_tables_query, get_date_tables_query


class Dataset:
    """
    --------------------
    Description
    --------------------
    -> Dataset (class): Class that manages a dataset loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> df (pd.Dataframe): Pandas dataframe where the table content has been loaded (mandatory)
    -> n_rows (int): Number of rows of dataset (optional)
    -> n_cols (int): Number of columns of dataset (optional)
    -> n_duplicates (int): Number of duplicated rows of dataset (optional)
    -> n_missing (int): Number of missing values of dataset (optional)
    -> num_cols (list): List of columns of numerical type (optional)
    -> text_cols (list): List of columns of text type (optional)
    -> date_cols (list): List of columns of datetime type (optional)
    """
    def __init__(self, schema_name=None, table_name=None, db=None, df=None):
        #=> To be filled by student
        self.schema_name = schema_name
        self.table_name = table_name
        self.db = db
        sqlquery = "select * from " + self.table_name
        self.df = pd.read_sql_query(sqlquery,db.conn)
        self.n_rows = 0
        self.n_cols = 0
        self.n_duplicates = 0
        self.n_missing = 0
        self.num_cols = []
        self.text_cols = []
        self.date_cols = []

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes 
        all requested information from self.df 
        to be displayed in the Overall section of Streamlit app 

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        # => To be filled by student
        #if self.is_df_none() == False:
        self.set_dimensions()
        st.write("sudah")
        self.set_duplicates()
        self.set_missing()
        self.set_numeric_columns()
        self.set_date_columns()
        self.set_text_columns()
        #st.session_state['data'] = self
        
    def is_df_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_df_none (method): Class method that checks if self.df is empty or none 

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        return self.df.empty 

    def set_dimensions(self):
        """
        --------------------
        Description
        --------------------
        -> set_dimensions (method): Class method that computes the dimensions (number of columns and rows) of self.df and store them as attributes (self.n_rows, self.n_cols)

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        self.n_rows = self.df.shape[0]
        self.n_cols = self.df.shape[1]

    def set_duplicates(self):
        """
        --------------------
        Description
        --------------------
        -> set_duplicates (method): Class method that computes the number of duplicated of self.df and store it as attribute (self.n_duplicates)

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        self.n_duplicates = self.df[self.df.duplicated()]

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing values of self.df and store it as attribute (self.n_missing)

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        self.n_missing = self.df.isnull().sum().sum()

    def set_numeric_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_numeric_columns (method): Class method that 
        extract the list of numeric columns from a table using a SQL query 
        (from get_numeric_tables_query()),
        store it as attribute (self.num_cols) and 
        then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        query = get_numeric_tables_query(self.schema_name, self.table_name)
        self.df = self.db.run_query(query)
        #print(self.df)
        self.num_cols = self.df["table_name"].values.tolist()

    def set_text_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_text_columns (method): Class method that extract the 
        list of text columns from a table using a SQL query 
        (from get_numeric_tables_query()),
        store it as attribute (self.text_cols) and 
        then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        query = get_text_tables_query(self.schema_name, self.table_name)
        self.df = self.db.run_query(query)
        #print(self.df)
        self.text_cols = self.df["table_name"].values.tolist()

    def set_date_columns(self):
        """
        --------------------
        Description
        --------------------
        -> set_date_columns (method): Class method that extract the list of datetime columns from a table using a SQL query (from get_numeric_tables_query()),
        store it as attribute (self.date_cols) and then convert the relevant columns of self.df accordingly.

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        query = get_date_tables_query(self.schema_name, self.table_name)
        self.df = self.db.run_query(query)
        self.date_cols  = self.df["table_name"].values.tolist()

    def get_head(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        return self.df.head(n)

    def get_tail(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_tail (method): Class method that computes the last rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        return self.df.tail(n)

    def get_sample(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_sample (method): Class method that computes a random sample of rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        return self.df.sample(n)

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats 
        all requested information from self.df to be displayed 
        in the Overall section of Streamlit app as 
        a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => To be filled by student
        -> pseudo-code

        --------------------
        Returns
        --------------------
        => To be filled by student
        -> (type): description

        """
        #=> To be filled by student
        self.df = pd.DataFrame({'Description':['Table Name',
                                        'Number of Rowss',
                                        'Number of Columns',
                                        'Number of Duplicated Rows',
                                        'Number of Rows with Missing Values'
                                        ],
                    'Values':[str(self.table_name),
                                str(self.n_rows),
                                str(self.n_cols),
                                str(self.n_duplicates),
                                str(self.n_missing),
                                ]})
        return self.df
