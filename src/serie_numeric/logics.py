import pandas as pd
import altair as alt

from src.database.logics import PostgresConnector
from src.serie_numeric.queries import get_negative_number_query, get_std_query, get_unique_query

class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column loaded from Postgres

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
    -> col_mean (int): Average value of a serie (optional)
    -> col_std (int): Standard deviation value of a serie (optional)
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> col_median (int): Median value of a serie (optional)
    -> n_zeros (int): Number of times a serie has values equal to 0 (optional)
    -> n_negatives (int): Number of times a serie has negative values (optional)
    -> histogram (int): Altair histogram displaying the count for each bin value of a serie (optional)
    -> frequent (int): Datframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, schema_name, table_name, col_name) -> None:
        
        
        self.df = pd.DataFrame()
        self.serie = None
        # not sure why PostgresConnector require both database and host 
        self.db = PostgresConnector(session_states['db_host'],
                          session_states['db_user'],
                          session_states['db_pass'],
                          session_states['db_host'],
                          session_states['db_port']
                          )
        self.schema_name = schema_name
        self.table_name = table_name
        self.col_name = col_name
        
        self.n_unique = None
        self.col_mean = None
        self.col_std = None
        self.col_min = None
        self.col_max = None
        self.col_median = None
        self.n_missing = None
        
        self.n_negatives = None
        self.histogram = None
        self.frequent = None
    
    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Numeric section of Streamlit app 

        --------------------
        Parameters
        --------------------
        pass
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        -> pseudo-code
        call all the methods: 
        set_zeros()
        set_missing()
        set_negatives()
        set_unique()
        set_mean()
        set_min()
        set_max()
        set_median()
        set_std()
        --------------------
        Returns
        --------------------
        all the requested information
        """
        self.set_zeros()
        self.set_missing()
        self.set_negatives()
        self.set_unique()
        self.set_mean()
        self.set_min()
        self.set_max()
        self.set_median()
        self.set_std()

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        return None if self.serie is empty or none  

        --------------------
        Returns
        --------------------
        boolean

        """
        return self.serie == None

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a column using a SQL query (get_unique_query())

        --------------------
        Parameters
        --------------------
        
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        pass
        -> pseudo-code

        --------------------
        Returns
        --------------------
        pass
        -> (type): description

        """
        
        self.n_unique = self.db.run_query(get_unique_query(self.schema_name,
                                                                           self.table_name,
                                                                           self.col_name)).count().item()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie

        --------------------
        Parameters
        --------------------
        column

        --------------------
        Pseudo-Code
        --------------------
        sum all the null in column

        --------------------
        Returns
        --------------------
        the number of null(int)

        """
        self.n_missing = self.serie.isnull().sum().item()


    def set_zeros(self):
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that computes the number of times a serie has values equal to 0

        --------------------
        Parameters
        --------------------
        column 

        --------------------
        Pseudo-Code
        --------------------
        count the number of 0 in each column

        --------------------
        Returns
        --------------------
        number of times a serie has values equal to 0 (int)

        """
        self.n_zeros = self.serie[self.serie == 0].count().item()

    def set_negatives(self):
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that computes the number of times a serie has negative values using a SQL query (get_negative_number_query())

        --------------------
        Parameters
        --------------------
        pass
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        pass
        -> pseudo-code

        --------------------
        Returns
        --------------------
    
        -> number of times a serie has negative values(int)

        """
      
        self.n_negatives = self.db.run_query(get_negative_number_query(self.schema_name,
                                                                       self.table_name,
                                                                       self.col_name)).count().item()

    def set_mean(self):
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that computes the average value of a serie

        --------------------
        Parameters
        --------------------
        column

        --------------------
        Pseudo-Code
        --------------------
        computes the average value of a serie

        --------------------
        Returns
        --------------------
        pass
        -> mean(int): average value of a serie

        """
        self.col_mean = self.serie.mean().item()

    def set_std(self):
        """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that computes the standard deviation value of a serie using a SQL query (get_std_query)

        --------------------
        Parameters
        --------------------
        serie

        --------------------
        Pseudo-Code
        --------------------
        
        -> pseudo-code

        --------------------
        Returns
        --------------------
        pass
        -> standard deviation(int): standard deviation value of a serie using a SQL query

        """
       
        res_df = self.db.run_query(get_std_query(self.schema_name,
                                                                 self.table_name,
                                                                 self.col_name))
        self.col_std = res_df.iloc[0].item()
    
    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie

        --------------------
        Parameters
        --------------------
        serie

        --------------------
        Pseudo-Code
        --------------------
        computes the minimum value of a serie

        --------------------
        Returns
        --------------------
        pass
        minimum value of a serie (int)

        """
        self.col_min = self.serie.min().item()

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie

        --------------------
        Parameters
        --------------------
        serie

        --------------------
        Pseudo-Code
        --------------------
        computes the maximum value of a serie

        --------------------
        Returns
        --------------------
        maximum value of a serie (int)

        """
        self.col_max = self.serie.max().item()

    def set_median(self):
        """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that computes the median value of a serie

        --------------------
        Parameters
        --------------------
        serie

        --------------------
        Pseudo-Code
        --------------------
        computes the median value of a serie

        --------------------
        Returns
        --------------------
        pass
        median value of a serie(int)

        """
        self.col_median = int(self.serie.median().item())


    def set_histogram(self):
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that computes the Altair histogram displaying the count for each bin value of a serie

        --------------------
        Parameters
        --------------------
        pass
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        pass
        -> pseudo-code

        --------------------
        Returns
        --------------------
        pass
        -> (type): description

        """
        self.histogram = alt.Chart(self.serie).mark_bar().encode(
            alt.X(f'{self.col_name}', bin=alt.BinParams(maxbins = 50)),
            alt.Y(f'count({self.col_name})'),
        )
        

    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie

        --------------------
        Parameters
        --------------------
        serie

        --------------------
        Pseudo-Code
        --------------------
        calculate the percentage with value 
        calculate the occurrence with value 
        combine the percentage and occurrence by value

        --------------------
        Returns
        --------------------
        the most frequest value of a serie


        """
        t = pd.DataFrame(self.serie[f'{self.col_name}'].value_counts(normalize =True))
        t = t.reset_index()
        t.columns = ['value', 'percentage']
        
        d =  pd.DataFrame(self.serie[f'{self.col_name}'].value_counts())
        d = d.reset_index()
        d.columns = ['value', 'occurrence']
        d = d.sort_values(by='value')
        d = d.reset_index(drop=True)
        
        d = d.join(t.set_index('value'), on='value')
        d = d.sort_values(by='occurrence', ascending=False)
        d = d.reset_index(drop=True)
        
        self.frequent = d.head(end)
        
        

    def get_summary_df(self) -> pd.DataFrame:
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        self.n_unique
        self.n_missing,
        self.n_zeros,
        self.n_negatives,
        self.col_mean,
        self.col_std,
        self.col_min,
        self.col_max,
        self.col_median

        --------------------
        Pseudo-Code
        --------------------
        formats all requested information

        --------------------
        Returns
        --------------------
        summary table

        """
        self.df = pd.DataFrame({'Description':['Number of Unique Values',
                                                'Number of Rows with Missing Values',
                                               'Number of Rows with 0',
                                               'Number of Rows with Negative Values',
                                               'Average Value',
                                               'Standard Deviation Value',
                                               'Minimum Value',
                                               'Maximum Value',
                                               'Median Value'
                                               ],
                            'Values':[str(self.n_unique),
                                      str(self.n_missing),
                                      str(self.n_zeros),
                                      str(self.n_negatives),
                                      str(self.col_mean),
                                      str(self.col_std),
                                      str(self.col_min),
                                      str(self.col_max),
                                      str(self.col_median)
                                      ]})
        return self.df

