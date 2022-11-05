import streamlit as st

from src.serie_date.logics import DateColumn

def display_dates():
    """
    --------------------
    Description
    --------------------
    -> display_dates (function): Function that displays all the relevant 
    information for every datetime column of a table

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
    st.write(dt)
    dt.set_data()
    lstOfDateColumn = dt.date_cols
    for i in range(len(lstOfDateColumn)):
        display_date(lstOfDateColumn[i],i)
    
    

def display_date(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_date (function): Function that instantiates a DateColumn 
    class from a dataframe column and displays all the relevant 
    information for a single datetime column of a table

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
    dateColumn =  DateColumn(schema_name,table_name,col_name)
    with st.expander("Date Information Column"):
        st.write(i+". " + col_name)
        st.table(dateColumn.get_summary_df())
