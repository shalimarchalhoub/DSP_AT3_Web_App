import streamlit as st

from src.dataframe.logics import Dataset

def read_data():
    """
    --------------------
    Description
    --------------------
    -> read_data (function): Function that 
    loads the content of the Postgres table selected, 
    extract its schema information and instantiate a 
    Dataset class accordingly

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
    schema_name = st.session_state['schema_selected']
    table_name = st.session_state['table_selected']
    db = st.session_state['db']
    dt = Dataset(schema_name, table_name, db)
    st.session_state['data'] = dt
    dt.set_data()

def display_overall():
    """
    --------------------
    Description
    --------------------
    -> display_overall (function): Function that displays 
    all the information on the Overall section of the streamlit app

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
    dt = st.session_state['data']
    st.dataframe(dt.get_summary_df())

def display_dataframes():
    """
    --------------------
    Description
    --------------------
    -> display_dataframes (function): Function that displays 
    all the information on the Explore section of the streamlit app

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
    dt = st.session_state['data']
    st.dataframe(dt.df)
