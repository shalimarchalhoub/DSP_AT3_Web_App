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
    => No parameters

    --------------------
    Pseudo-Code
    --------------------
    => This function reads the Postgres table and select the needed information

    --------------------
    Returns
    --------------------
    => This function does not return anything

    """
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
    => No parameters

    --------------------
    Pseudo-Code
    --------------------
    => This function is used to display the section Overall on the web app

    --------------------
    Returns
    --------------------
    => This function does not return anything
    """
    schema_name = st.session_state['schema_selected']
    table_name = st.session_state['table_selected']
    dt = st.session_state['data']
    st.dataframe(dt.get_summary_df())
    db = st.session_state['db']
    st.dataframe(db.get_table_schema(schema_name,table_name))
    

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
    => No parameters

    --------------------
    Pseudo-Code
    --------------------
    => This function is made to display the needed information for the Explore section on the web app

    --------------------
    Returns
    --------------------
    => This function does not return anything

    """
    st.write('Explore Dataframe')
    dt = st.session_state['data']
    mxrow = dt.n_rows
    nrow = st.slider('Select the number of rows to be displayed', min_value=5, max_value=mxrow)
    method = st.radio("Exploration Method",('Head', 'Tail', 'Sample'))

    if method == 'Head':
        st.write('Top Rows of Selected Table')
        st.dataframe(dt.get_head(nrow))
    elif method == 'Tail':
        st.write("Bottom Rows of Selected Table")
        st.dataframe(dt.get_tail(nrow))
    elif method == 'Sample':
        st.write("Random Sample Rows of Selected Table")
        st.dataframe(dt.get_sample(nrow))
    
