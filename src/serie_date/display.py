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
    dt.set_data()
    lstOfDateColumn = dt.date_cols
    for i in range(len(lstOfDateColumn)):
        display_date(lstOfDateColumn[i],(i+1))
