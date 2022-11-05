import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import sys
from src.database.logics import PostgresConnector
from src.serie_text.queries import get_missing_query, get_mode_query, get_alpha_query
from src.serie_date.queries import get_column_query

sys.path.insert(0, '../../')
session_states = {'db':'', 'db_host':'', 'db_name':'', 'db_port':'',
              'db_user':'', 'db_pass':'', 'db_status':'',
              'db_infos_df':'', 'schema_selected':'', 
              'table_selected':'', 'data':''}

session_states['table_name'] = ''

class TextColumn:
    """
    --------------------
    Description
    --------------------
    -> TextColumn (class): Class that manages a column loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> col_name (str): Name of the column (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (mandatory)
    -> n_unique (int): Number of unique value of a serie (optional)
    -> n_missing (int): Number of missing values of a serie (optional)
    -> n_empty (int): Number of times a serie has empty value (optional)
    -> n_mode (int): Mode value of a serie (optional)
    -> n_space (int): Number of times a serie has only space characters (optional)
    -> n_lower (int): Number of times a serie has only lowercase characters (optional)
    -> n_upper (int): Number of times a serie has only uppercase characters (optional)
    -> n_alpha (int): Number of times a serie has only alphabetical characters (optional)
    -> n_digit (int): Number of times a serie has only digit characters (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Datframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, schema_name=None, table_name=None, col_name=None, db=None, serie=None):
        self.schema_name: str = schema_name
        self.table_name: str = table_name 
        self.col_name: str = col_name
        self.df = pd.DataFrame()
        self.db = PostgresConnector(session_states['db_host'],
                                    session_states['db_user'],
                                    session_states['db_pass'],
                                    session_states['db_host'],
                                    session_states['db_port'])
        self.serie: pd.Series = serie
        self.n_unique: int = None
        self.n_missing: int = None
        self.n_empty: int = None
        self.n_mode: int = None
        self.n_space: int = None
        self.n_lower: int = None
        self.n_upper: int = None
        self.n_alpha: int = None
        self.n_digit: int = None
        self.barchart: int = None
        self.frequent: int = None
    
    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Text section of Streamlit app 

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Return information for 
        is_serie_none()
        set_unique()
        set_missing()
        set_empty()
        set_mode()
        set_whitespace()
        set_lowercase()
        set_uppercase()
        set_alphabet()
        set_digit()
        set_barchart()
        set_frequent()

        --------------------
        Returns
        --------------------
        return information for all the logic queries

        """
        self.is_serie_none()
        self.set_unique()
        self.set_missing()
        self.set_empty()
        self.set_mode()
        self.set_whitespace()
        self.set_lowercase()
        self.set_uppercase()
        self.set_alphabet()
        self.set_digit()
        self.set_barchart()
        self.set_frequent()

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        check if series is empty and return answer

        --------------------
        Returns
        --------------------
        (Boolean)-> : 
        True if empty
        False if not empty

        """
        return bool(self.serie)

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Get the unique values of a serie in a list
        Count number of items in the list
        Return appropriate value 


        --------------------
        Returns
        --------------------
        -> (int): number of unique values in a serie

        """
        return len(self.serie.unique().tolist())

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie using a SQL query (get_missing_query())

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Get the sum of the missing values in the series using the sql query get_missin_query()
        Return appropriate value

        --------------------
        Returns
        --------------------
        (int): Number of missing values

        """
        return get_missing_query(self.schema_name, self.table_name, self.col_name)


    def set_empty(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty (method): Class method that computes the number of times a serie has empty value

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Get the empty values of the series
        Return the sum of empty values

        --------------------
        Returns
        --------------------
        (int): Number of empty values


        """
        empty = self.serie.values == ''
        return empty.sum()

    def set_mode(self):
        """
        --------------------
        Description
        --------------------
        -> set_mode (method): Class method that computes the mode value of a serie using a SQL query (get_mode_query())

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Use the get_mode_query using the schema_name, table_name and col_name attributes

        --------------------
        Returns
        --------------------
        (string): mode value of a serie

        """
        return (get_mode_query(self.schema_name, self.table_name, self.col_name))

    def set_whitespace(self):
        """
        --------------------
        Description
        --------------------
        -> set_whitespace (method): Class method that computes the number of times a serie has only space characters

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Check the serie for entries that are white spaces and return the sum of them

        --------------------
        Returns
        --------------------
        (int): Number of white space values

        """
        return sum(self.serie.str.isspace())

    def set_lowercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_lowercase (method): Class method that computes the number of times a serie has only lowercase characters

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Create an empty list
        do a loop in the serie and check if i is a number
        if it's a number return nothing but if it's an alphabet letter append it to the list
        create a new list that has all the alphabet entries to it
        sum the total number of times where the alphabet letters were in lower case letters

        --------------------
        Returns
        --------------------
        -> (int): number of entries with lowercase letters

        """
        alphabet = []
        for i in self.serie:
            if i is np.NaN:
                None
            else:
                if i.isalpha() == True:
                 alphabet.append(i)
        total= pd.Series(alphabet)
    
        return sum(total.str.islower().fillna(False))

    def set_uppercase(self):
        """
        --------------------
        Description
        --------------------
        -> set_uppercase (method): Class method that computes the number of times a serie has only uppercase characters

         --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Create an empty list
        do a loop in the serie and check if i is a number
        if it's a number return nothing but if it's an alphabet letter append it to the list
        create a new list that has all the alphabet entries to it
        sum the total number of times where the alphabet letters were in upper case letters

        --------------------
        Returns
        --------------------
        -> (int): number of entries with upper letters
        """

        alphabet = []
        for i in self.serie:
            if i is np.NaN:
                None
            else:
                if i.isalpha() == True:
                 alphabet.append(i)
        total= pd.Series(alphabet)
    
        return sum(total.str.isupper().fillna(False))

    
    def set_alphabet(self):
        """
        --------------------
        Description
        --------------------
        -> set_alphabet (method): Class method that computes the number of times a serie has only alphabetical characters using a SQL query (get_alpha_query())

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        using the get_alpha_query with the arguments schema_name, table_name and col_name

        --------------------
        Returns
        --------------------
        int: total of times an entry is only alphabetical

        """
        return get_alpha_query(self.schema_name, self.table_name, self.col_name)

    def set_digit(self):
        """
        --------------------
        Description
        --------------------
        -> set_digit (method): Class method that computes the number of times a serie has only digit characters

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Check the serie for entries that contain only digit characters and and return the sum of them


        --------------------
        Returns
        --------------------
        (int): Number of entries with only digit characters

        """
        return sum(self.serie.str.isdigit())

    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Define data as column name of the series
        Create a Tabluar data chart from the defined data and create the Bar Chart with x as column name and y as the count
        return the Bar Chart

        --------------------
        Returns
        --------------------
        (chart): Bar Chart represeting the count of each value in a serie 

        """
        data = {self.col_name:self.serie} 
        BarChart = alt.Chart(pd.DataFrame(data)).mark_bar().encode(x=self.col_name, y='count()')
        return BarChart
      
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Define frequency as a count of all the values and reset it to 0
        Define the columns of the table as "Values" and "Occurance"
        Get the percentage of each occurence
        Return the top 20 values

        --------------------
        Returns
        --------------------
        -> (serie): 20 of the most frequent values

        """
        frequency = self.serie.value_counts().reset_index()
        frequency.columns = ['Values', 'Occurence']
        frequency['Percentage'] = (frequency['Occurence'] / frequency['Occurence'].sum()) * 100

        return frequency.head(20)

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        None

        --------------------
        Pseudo-Code
        --------------------
        Define summary as Pandas dataframe
        Create the column Description with all the apppropriate values
        Create the column value with all the appropriate values matching the column description
        Return the dataframe

        --------------------
        Returns
        --------------------
        Pandas Dataframe with 2 Columns

        """
        summary = pd.DataFrame()
        summary['Description'] = ['Number of Unique Values', 'Number of Rows with Missing Values', 'Number of Empty Rows', 'Number of Rows With Only Whitespace','Number of Rows with Only Lowercase', 'Number of Rows With Only Uppercase', 'Number of Rows with Only Alphabet', 'Number of Rows with Only Digits', 'Mode Value']
        summary['Value'] = [str(self.set_unique()), str(self.set_missing()), str(self.set_empty()), str(self.set_whitespace), str(self.set_lowercase), str(self.set_uppercase()), str(self.set_alphabet()), str(self.set_digit()), str(self.set_mode())]
        return summary
