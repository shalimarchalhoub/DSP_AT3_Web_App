import streamlit as st
import pandas as pd
import altair as alt

from src.database.logics import PostgresConnector
from src.serie_date.queries import get_min_date_query, get_weekend_count_query, get_1900_count_query

class DateColumn:
    """
    --------------------
    Description
    --------------------
    -> DateColumn (class): Class that manages a column loaded from Postgres

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
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> n_weekend (int): Number of times a serie has dates falling during weekend (optional)
    -> n_weekday (int): Number of times a serie has dates not falling during weekend (optional)
    -> n_future (int): Number of times a serie has dates falling in the future (optional)
    -> n_empty_1900 (int): Number of times a serie has dates equal to '1900-01-01' (optional)
    -> n_empty_1970 (int): Number of times a serie has dates equal to '1970-01-01' (optional)
    -> barchart (int): Altair barchart displaying the count for each value of a serie (optional)
    -> frequent (int): Dataframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, schema_name=None, table_name=None, col_name=None, db=None, serie=None):
        self.schema_name = schema_name
        self.table_name = table_name
        self.col_name = col_name
        self.db = db 
        self.serie = serie
        self.n_unique = 0
        self.n_missing = 0
        self.col_min = 0
        self.col_max = 0
        self.n_weekend = 0
        self.n_weekday = 0
        self.n_future = 0
        self.n_empty_1900 = 0
        self.n_empty_1970 = 0
        self.barchart = 0
        self.frequent = 0

    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Date section of Streamlit app 

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        Function that computes all the methods needed and store the results in this function, waiting to be called

        --------------------
        Returns
        --------------------
        This function only computes the methods, not returning anything

        """
        if not self.is_serie_none():
            self.set_unique()
            self.set_missing()
            self.set_min()
            self.set_max()

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => A function that checks whether the df is empty ot not and returns True or False according to the result

        --------------------
        Returns
        --------------------
        => True: when the df is empty
        => False: when the df is not empty
        """
        return self.serie.empty


    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a serie

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => A function that checks whether the unique values of a series and compute them

        --------------------
        Returns
        --------------------
        => The function only computes the total number of unique value in the serie, not returning anything

        """
        self.n_unique = self.serie.nunique()

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => A function that computes the total missing value in the column, not returning anything

        --------------------
        Returns
        --------------------
        => This function only computes the count, not returning anything

        """
        self.n_missing = self.serie.isnull().sum().sum()

    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie using a SQL query (get_min_date_query())

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => A function that calculates the minimum date in the column using the the function get_min_date_query from serie_date queries.py
        --------------------
        Returns
        --------------------
        => This function only computes/calculates the minimum date, does not return anything
        """
        self.col_min = self.db.run_query(get_min_date_query())

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => A function that calculates the maximum date in the column 
        --------------------
        Returns
        --------------------
        => This function only computes/calculates the maximum date, does not return anything

        """
        self.col_max = self.serie.max()

    def set_weekend(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekend (method): Class method that computes the number of times a serie has dates falling during weekend using a SQL query (get_weekend_count_query())

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function computes the count of weekend days in the column using query from query.py file, the get_weekend_count_query() function
        --------------------
        Returns
        --------------------
        => This function only computes the total count, but does not return anything

        """
        self.n_weekend = self.db.run_query(get_weekend_count_query())

    def set_weekday(self):
        """
        --------------------
        Description
        --------------------
        -> set_weekday (method): Class method that computes the number of times a serie has dates not falling during weekend

        --------------------
        Parameters
        --------------------
        => No parameters
        --------------------
        Pseudo-Code
        --------------------
        => This function computes the count of weekdays in the column

        --------------------
        Returns
        --------------------
        => This function only computes the count of dates falling on weekdays, but does not return anything

        """
        if self.serie.dt.weekday<5:
            self.n_weekday = self.serie.dt.weekday.count()

    def set_future(self):
        """
        --------------------
        Description
        --------------------
        -> set_future (method): Class method that computes the number of times a serie has dates falling in the future

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function calculates the dates in the future counted from today 

        --------------------
        Returns
        --------------------
        => This function only calculates the method, it does not return anything

        """
        present_date = pd.Timestamp.today() 
        for dates in self.serie:
            if dates>present_date:
                self.n_future += 1

    def set_empty_1900(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1900 (method): Class method that computes the number of times a serie has dates equal to '1900-01-01' using a SQL query (get_1900_count_query())

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => The function that calculates how many dates in the column are equal to 1900-01-01 using the query from serie_date query.py get_1900_count_query() function
        --------------------
        Returns
        --------------------
        => This function does not return anything, only calculating the count of dates falling on 1900-01-01

        """
        self.n_weekend = self.db.run_query(get_weekend_count_query())

    def set_empty_1970(self):
        """
        --------------------
        Description
        --------------------
        -> set_empty_1970 (method): Class method that computes the number of times a serie has dates equal to '1970-01-01'

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function calculates the count of dates in the column falling on 1970-01-01

        --------------------
        Returns
        --------------------
        => This function only computes the count of dates falling on 1970-01-01 and returns nothing

        """
        for dates in self.serie:
            new = pd.Series("dates")

            day = pd.to_datetime(new).dt.day
            day.values
            newday = list(day)

            month = pd.to_datetime(new).dt.month
            month.values
            newmonth = list(month)

            year = pd.to_datetime(new).dt.year
            year.values
            newyear = list(year)
            
            if (str(newyear) == '1970' and str(newmonth) == '01' and str(newday) == '01'):
                self.n_empty_1970 += 1

    def set_barchart(self):  
        """
        --------------------
        Description
        --------------------
        -> set_barchart (method): Class method that computes the Altair barchart displaying the count for each value of a serie

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => This function processes the barchart using Altair library using the count for each value in accordance to their date time

        --------------------
        Returns
        --------------------
        => This function does not return anything

        """
        count_serie = self.serie.count()
        dataframed = pd.DataFrame(count_serie, columns=["Date Time", "Count"])
        self.barchart = alt.Chart(dataframed).mark_bar().encode(x = "Date Time", y = "Count", color = 'c')
        return self.barchart
      
    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie

        --------------------
        Parameters
        --------------------
        => To be filled by student
        -> name (type): description

        --------------------
        Pseudo-Code
        --------------------
        => This function calculates the top 20 most frequent values in the serie and store them in a dataframe

        --------------------
        Returns
        --------------------
        => This function only calculates the top 20 most frequent values, it does not return anything

        """
        MyDict={}

        newserie = self.serie.to_string()
        for dates in newserie: 
            MyDict[dates] = MyDict.get(dates, 0)+1
        
        newdf = pd.DataFrame([MyDict.keys,MyDict.values])
        newdf['percent'] = newdf[MyDict.values]*100/len(MyDict.values)
        newdf = newdf.head(20)
        self.frequent = newdf

    def get_summary_df(self):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

        --------------------
        Parameters
        --------------------
        => No parameters

        --------------------
        Pseudo-Code
        --------------------
        => A function that puts all the variables previously stored into a dataframe containing its name/description along with the values.

        --------------------
        Returns
        --------------------
        => The function returns the dataframe containing all the values stored, along with the column names

        """
        st.header(self.col_name)
        dfdate = pd.DataFrame({'Description':['Number of Unique Values',
                                               'Number of Missing Values',
                                               'Number of Occurrence of Days Falling During Weekend',
                                               'Number of Weekday Days',
                                               'Number of Cases with Future Dates',
                                               'Number of Occurrence of 1900-01-01 value',
                                               'Number of Occurrence of 1970-01-01 value',
                                               'The Minimum Date',
                                               'The Maximum Date'
                                               ],
                            'Values':[str(self.n_unique),
                                      str(self.n_missing),
                                      str(self.n_weekend),
                                      str(self.n_weekday),
                                      str(self.n_future),
                                      str(self.n_empty_1900),
                                      str(self.n_empty_1970),
                                      str(self.col_min),
                                      str(self.col_max)
                                      ]})

        return dfdate
