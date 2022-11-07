import streamlit as st

from src.dataframe.logics import Dataset
from src.serie_numeric.logics import NumericColumn

def display_numerics(dataset:Dataset):
    """
    --------------------
    Description
    --------------------
    -> display_numerics (function): Function that displays all the relevant information for every numerical column of a table

    --------------------
    Parameters
    --------------------
    -> name (type): description
    col_name (any): the name of column
    i(int) : number of order
    --------------------
    Pseudo-Code
    --------------------
    for all the column: 
    combine the name and number of oder
    --------------------
    Returns
    --------------------
    disply the name of column and the order

    """
    for col_name, i in zip(dataset.num_cols, range(1,len(dataset.num_cols)+1)):
        display_numeric(col_name, i)
    
def display_numeric(col_name, i):
    """
    --------------------
    Description
    --------------------
    -> display_numeric (function): Function that instantiates a NumericColumn class from a dataframe column and displays all the relevant information for a single numerical column of a table

    --------------------
    Parameters
    --------------------
    -> name (type): description
    session_states(str) : 

    --------------------
    Pseudo-Code
    --------------------
    call the NumeriColumn()
    use expander to create summary table by calling the get_summary_df
    use expander to create summary table by calling the set_histogram()
    use expander to create summary table by calling the numeric_column.histogram
    --------------------
     Returns
    --------------------
    Return summary table, histogram and most frequent values table.

    """
    numeric_column = NumericColumn(session_states['schema_selected'],
                                   session_states['table_name'],
                                   col_name=col_name)
    

        
    
        
        