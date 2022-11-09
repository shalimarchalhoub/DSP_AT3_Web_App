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
    => No parameters
    --------------------
    Pseudo-Code
    --------------------
    => This function loops the display_date function to display every single column having 'date' data type
    --------------------
    Returns
    --------------------
    => This function does not return anything, only loops the display_date function and display the result for each column with 'Date' data type

    """
    dt = st.session_state['data']
    dt.set_data()
    lstOfDateColumn = dt.date_cols
    for i in range(len(lstOfDateColumn)):
        display_date(lstOfDateColumn[i],(i+1))
    
    

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
    => col_name (char) = displaying the name of the column with 'Date' data type in the displayed dataframe
    => i (int) = displaying the index/numbering of the above column
    --------------------
    Pseudo-Code
    --------------------
    => This function will return the name of the column (col_name), the indexing (i), along with the requested information needed as saved in set_data.
    --------------------
    Returns
    --------------------
    => This function does not return anything, only instantiates and displays the information for one column

    """
    db = st.session_state['db']
    schema_name = st.session_state['schema_selected']
    table_name = st.session_state['table_selected']
    dateColumn =  DateColumn(schema_name,table_name,col_name,db)
    dateColumn.set_data()
    with st.expander("Date Information Column"):
        st.write(str(i)+". " + col_name)
        st.table(dateColumn.get_summary_df())
        st.altair_chart(dateColumn.barchart, use_container_width=True)
        st.dataframe(dateColumn.frequent)
