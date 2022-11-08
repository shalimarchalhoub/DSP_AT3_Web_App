import streamlit as st

def set_app_config():
    """
    --------------------
    Description
    --------------------
    -> set_app_config (function): Function that sets the configuration of the Streamlit app

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

    st.set_page_config(
        page_title="Streamlit application for performing data exploration on a database",
        page_icon="random",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://streamlit.io',
            'Report a bug': 'https://github.com',
            'About': 'About your applicatioin: **data exploration on a database***'
        }
    )

def set_session_state(key, value):
    """
     --------------------
     Description
     --------------------
     -> set_session_state (function): Function that saves a key-value pair to the Streamlit session state

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

    if key not in st.session_state:
        st.session_state[key]=value
    for item in st.session_state.items():
        return item
def set_session_states(keys, value=None):
    """
    --------------------
    Description
    --------------------
    -> set_session_states (function): Function that saves a list of key-value pairs to the Streamlit
    session state using set_session_state() (default value: None)

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
    """
    if 'db' not in st.session_state:
        st.session_state.db='postgres'
    if 'db_host' not in st.session_state:
        st.session_state.db_host='127.0.0.1'
    if 'db_name' not in st.session_state:
        st.session_state.db_name='postgres'
    if 'db_user' not in st.session_state:
        st.session_state.db_user='postgres'
    if 'db_pass' not in st.session_state:
        st.session_state.db_pass='password'
    if 'db_status' not in st.session_state:
        st.session_state.db_status=_connect_form_cb
    if 'db_infos_df' not in st.session_state:
        st.session_state.db_infos_df=dt.info()
    if 'schema_selected' not in st.session_state:
        st.session_state.schema_selected=option.rpartition('.')[0]
    if 'table_selected' not in st.session_state:
        st.session_state.table_selected=option.rpartition('.')[2]
    if 'data' not in st.session_state:
       st.session_state.data=read_data
    for item in st.session_state.items():
        return(item)

def display_session_state():
    """
        --------------------
        Description
        --------------------
        -> display_session_state (function): Function that displays the current values of Streamlit session state

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
    for item in st.session_state.items():
        st.write(item)





