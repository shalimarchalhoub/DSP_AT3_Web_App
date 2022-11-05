
import streamlit as st

from src.serie_text.logics import TextColumn
from src.dataframe.logics import Dataset

def display_texts():
    """
    --------------------
    Description
    --------------------
    -> display_texts (function): Function that displays all the relevant information for every text column of a table

    --------------------
    Parameters
    --------------------
    None

    --------------------
    Pseudo-Code
    --------------------
    Define the database, schema and table
    Define the data from the Dataset(schema, table, db) function
    Use function setdata() from queries to display relevant information
    Define the column
    Do a for loop if the column is not none
    For every column, display the infromation in that column through an expander

    --------------------
    Returns
    --------------------
    Display all relevant information for a column

    """
    db = st.session_state['db']
    schema = st.session_state['schema_selected']
    table = st.session_state['table_selected']
    Data = Dataset(schema, table, db=db)

    Data.set_data()
    
    Column = Data.Column
    
    if Column is not None:
        for i, cols in enumerate(Column):
            with st.expander(f"{i+1}. column: {cols}"):
                display_text(cols, i)

def display_text(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_text (function): Function that instantiates a TextColumn class from a dataframe column and displays all the relevant information for a single text column of a table

    --------------------
    Parameters
    --------------------
    col_name (string): the name of the column of a table
    i (int): column index

    --------------------
    Pseudo-Code
    --------------------
    Define the database, schema and table
    Define the data from the TextColumn(schema, table, col_name, db) function
    Use function setdata() from queries to display relevant information
    Do a table with the data summary st.table
    Create a subheader using st.subheader
    Using Altair, create a barchart
    Create a subheader using st.subheader
    Display most frequent value using data.frequent

    --------------------
    Returns
    --------------------
    Displays all the relevant information for a single text column of a table

    """
    db = st.session_state['db']
    schema = st.session_state['schema_selected']
    table = st.session_state['table_selected']
    Data = TextColumn(schema, table, col_name, db=db)
    Data.set_data()

    st.table(data=Data.get_summary_df())
    st.subheader('Bar Chart')
    st.altair_chart(Data.barchart, use_container_width=True)
    st.subheader('Most Frequent Values')
    st.dataframe(data=Data.frequent)

import streamlit as st

from src.serie_text.logics import TextColumn

def display_texts():
    """
    --------------------
    Description
    --------------------
    -> display_texts (function): Function that displays all the relevant information for every text column of a table

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
    => To be filled by student

def display_text(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_text (function): Function that instantiates a TextColumn class from a dataframe column and displays all the relevant information for a single text column of a table

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
    => To be filled by student

