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
        self.schema_name = schema_name
        self.table_name = table_name
        self.db = db
        self.df = db.load_table(schema_name,table_name)
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
        => set_data (method): Class method that computes 
        all requested information from self.df 
        to be displayed in the Overall section of Streamlit app 

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => A function that computes the requested information from self.df as long as the df is not empty.

        --------------------
        Returns
        --------------------
        => Does not return anything, only computing and retaining the requested information

        """
        if self.is_df_none() == False:
            self.set_dimensions()
            self.set_duplicates()
            self.set_missing()
            self.set_numeric_columns()
            self.set_date_columns()
            self.set_text_columns()
            
    def is_df_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_df_none (method): Class method that checks if self.df is empty or none 

        --------------------
        Parameters
        --------------------
        => No parameters
        
        --------------------
        Pseudo-Code
        --------------------
        => The function checks whether the dataframe is empty or not, and returns True if empty and False if not empty.

        --------------------
        Returns
        --------------------
        => True: if df is empty
        => False: if df is not empty

        """
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
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => The function calculates the numeber of rows and columns in df and retains the information and store them to self.n_rows and self.n_cols while not returning anything
        
        --------------------
        Returns
        --------------------
        => This function only computes and stores information, does not return anything

        """
        self.n_rows = self.df.shape[0]
        self.n_cols = self.df.shape[1]

    def set_duplicates(self):
        """
        --------------------
        Description
        --------------------
        -> set_duplicates (method): Class method that computes 
        the number of duplicated of self.df and store 
        it as attribute (self.n_duplicates)

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function calculates the total number of dataframe duplicates but does not return anything, as it will only calculate the needed information and store in self.n_duplicates

        --------------------
        Returns
        --------------------
        => This function does not return anything

        """
        self.n_duplicates = self.df.duplicated().sum()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing values of self.df and store it as attribute (self.n_missing)

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function calculates the total sum of missing values in self.df and store the result in self.n_missing, but the function does not return anything

        --------------------
        Returns
        --------------------
        => This function does not return anything, only computes and stores the result in self.n_missing

        """
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
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function gets the numeric columns from postgres table using the get_numeric_tables_query() function and store them in self.num_cols
        
        --------------------
        Returns
        --------------------
        => This function does not return anything

        """
        query = get_numeric_tables_query(self.schema_name, self.table_name)
        numdf = self.db.run_query(query)
        self.num_cols = numdf["column_name"].values.tolist()

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
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function gets the numeric columns from postgres table using the get_text_tables_query() function and store them in self.text_cols

        --------------------
        Returns
        --------------------
        => This function does not return anything

        """
        query = get_text_tables_query(self.schema_name, self.table_name)
        textdf = self.db.run_query(query)
        self.text_cols = textdf["column_name"].values.tolist()

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
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function gets the numeric columns from postgres table using the get_date_tables_query() function and store them in self.date_cols
        
        --------------------
        Returns
        --------------------
        => This function does not return anything

        """
        query = get_date_tables_query(self.schema_name, self.table_name)
        datedf = self.db.run_query(query)
        self.date_cols  = datedf["column_name"].values.tolist()

    def get_head(self, n=5):
        """
        --------------------
        Description
        --------------------
        -> get_head (method): Class method that computes the first rows of self.df according to the provided number of rows specified as parameter (default: 5)

        --------------------
        Parameters
        --------------------
        => n (int) = the number of rows
        
        --------------------
        Pseudo-Code
        --------------------
        => This function displays and returns the top n rows of the df with default of 5.

        --------------------
        Returns
        --------------------
        => dataframe with n rows starting from the top

        """
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
        => n (int) = the number of rows

        --------------------
        Pseudo-Code
        --------------------
        => This function displays and returns the bottom n rows of the df with default of 5.

        --------------------
        Returns
        --------------------
        => dataframe with n rows starting from the bottom
        
        """
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
        => n (int) = the number of rows

        --------------------
        Pseudo-Code
        --------------------
        => This function displays and returns random n rows of the df with random orders with default of 5.

        --------------------
        Returns
        --------------------
        => dataframe with n rows at random orders
        
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
        => No parameters
        
        --------------------
        Pseudo-Code
        --------------------
        => This function makes a dataframe containing 2 columns, 'Description' and its 'Value', whose information has been calculated from set_data().

        --------------------
        Returns
        --------------------
        => The dataframe of the desired information in the Overall section of the app

        """
        infodf = pd.DataFrame({'Description':['Table Name',
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
        return infodf
