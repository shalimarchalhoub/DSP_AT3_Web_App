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
    ->page_title:It is used to setup the page title
    ->page_icon:It is used for setting up the page icon
    ->layout: It is used for setting up the layout
    ->initial_sidebar_state: It is used to initialise the sidebar state
    ->menu_items: It is used for setting up the menu items such as about,get help, etc.



    --------------------
    Pseudo-Code
    --------------------
    -> This code is used to set up the App config.

    --------------------
    Returns
    --------------------
    ->It returns the App conifguration

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
     ->key: Type is str, it stores the key given as one of the inputs
     ->value:Type is str, it stores the value given as one of the inputs

     --------------------
     Pseudo-Code
     --------------------
     -This code saves a key-value pair to the streamlit session state.

     --------------------
     Returns
     --------------------
     ->It returns the key-value pair to the streamlit session state.
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
    ->Keys: type is str, it takes the keys as an input
    ->items:type is str, it stores the list of key-value pair

    --------------------
    Pseudo-Code
    --------------------
    ->This code saves a list of key-value pairs to the Streamlit

    --------------------
    Returns
    --------------------
    ->return type is str, key-value pairs is returned
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
        st.session_state.db_status=connect_db()
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
        -> item: It stores the current values of streamlit session state.

        --------------------
        Pseudo-Code
        --------------------
        -> This code displays the current values of streamlit session state.

        --------------------
        Returns
        --------------------
        -> Type is str, it returns the current values of the streamlit session state.

        """
    for item in st.session_state.items():
        st.write(item)





