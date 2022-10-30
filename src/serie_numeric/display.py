import streamlit as st

# for debug only
# the session_states below should be provided after set_session_states() or set_app_config()
import sys
sys.path.insert(0, '../../')
import pandas as pd
session_states = {'db':'', 'db_host':'', 'db_name':'', 'db_port':'',
              'db_user':'', 'db_pass':'', 'db_status':'',
              'db_infos_df':'', 'schema_selected':'', 
              'table_selected':'', 'data':''}
session_states['table_name'] = ''
#


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
    col_name (variale): column name 
    --------------------
    Pseudo-Code
    --------------------
    for all the column: 
    combine the column name and number of oder
    --------------------
    Returns
    --------------------
    

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
    schema_selected: 
    table_name:
    col_name: 
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
    numeric_column = NumericColumn(session_states['schema_selected'],
                                   session_states['table_name'],
                                   col_name=col_name)
    
    # for debug only
    if debug:
        numeric_column = NumericColumn( 'postgres','student', 'inte')
        numeric_column.serie = pd.DataFrame({'inte': [-1,-4,7,50,7,7,7,7,7,7]})
    #
    
    with st.expander(f"{i}. Column: {col_name}"):
        numeric_column.set_data()
        st.table(numeric_column.get_summary_df())
        
        st.text('Histogram')
        numeric_column.set_histogram()
        
        print(numeric_column.histogram)
        
        st.altair_chart(numeric_column.histogram)
        
        st.text("Most Frequence Values")
        numeric_column.set_frequent()
        st.table(numeric_column.frequent)


if __name__ == '__main__':
    # To check this page, 
    # cd to dsp_at3_student_id\src\serie_numeric
    # streamlit run display.py
    debug = True
    display_numeric('inte', 1)
    display_numeric('inte', 2)
    display_numeric('inte', 3)
    #
        
    
        
        