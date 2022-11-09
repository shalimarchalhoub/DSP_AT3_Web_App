import streamlit as st
import pandas as pd
import psycopg2
from psycopg2 import OperationalError
from src.database.logics import PostgresConnector
from src.dataframe.display import read_data




def display_db_connection_menu():

    """
     ------
     display_db_connection_menu-> This functions display the menu to connect
     to the database
     ------
     Parameters
     ------
     ->username: type is str, it stores the username entered by the user
     ->password: type is str, it stores the password entered by the user
     ->db_Name: type is str, it stores the databse name entered by the user
     ->db_Host: type is str, it stores the host name entered by the user
     ->db_port: type is str,It sotres the port number entered by the user.
     ->conn: type is str, it stores the connection to the Postgres database

     -------
     pseudo-code--
     ----
     -> This code creates a menu button, where the user can enter the details to login
     to the Postgres database
     ---
     return
     ---
     ->type is str,it displays on the screen whether the user is succesfully connected to
     the databse, or the attempt was unsuccesful.Also, it returns the connection establishement so that
     the user can pull or push data/request to the Postgres databse.
     ----
    """
    if 'CONNECTED' not in st.session_state:
        st.session_state.CONNECTED = False

    def _connect_form_cb(connect_status):
        st.session_state.CONNECTED = connect_status

    with     st.form(key="my_form"):
             global username
             username = st.text_input("Username:")
             global password
             password = st.text_input("Password:",type="password")
             global db_Host
             db_Host = st.text_input("Database Host:")
             global db_Name
             db_Name = st.text_input("Database Name:")
             global db_port
             db_Port = st.text_input("Database Port:")
             global submit
             global conn
             conn=None
             submit = st.form_submit_button("🟢 Connect", on_click=_connect_form_cb, args=(True,),
                                            disabled=st.session_state.CONNECTED)

             if st.session_state.CONNECTED:
                try:
                    conn = psycopg2.connect("""dbname={0} user={1}
                                                 password
                                                 ={2}""".format(db_Name, username, password))
                    st.write("connection to database established")

                except (Exception,psycopg2.DatabaseError) as error:
                    st.write(error)



def connect_db():
    """
        --------------------
        Description
        --------------------
        -> connect_db (function): Function that connects to a database and instantiate a PostgresConnector
        class accordingly

        --------------------
        Parameters
        --------------------
        ->connectdb:type is Object, Object used to instantiate PostgresConnector class

        --------------------
        Pseudo-Code
        --------------------
        ->This code hepls connect to a database  and instantiate a PostgresConnector
        class accordingly

        --------------------
        Returns
        --------------------
        ->It returns the connection to the database

        """
    if submit:
       connectdb=PostgresConnector('{}'.format(db_Name),'{}'.format(username),'{}'.format(password))
       connection=connectdb.open_connection()
       print("connection to the database is established and class instantiated")
       return connection

def display_table_selection():
    """
        --------------------
        Description
        --------------------
        -> display_table_selection (function): Function that displays the selection box for selecting the
        table to be analysed and triggers the loading of data (read_data())

        --------------------
        Parameters
        --------------------
        ->cursor: type is cursor datatype, It is used to hold the connection to the database
        so that the user can do a transaction
        ->data: type is string/two-dimensional tabular structure ,It holds the data fetched by the cursor from the database.
        ->df: type is string/two-dimensional tabular structure with labelled axes(rows and columns). It holds the information
        after being converted into a dataframe.

        --------------------
        Pseudo-Code
        --------------------
        ->This code produces the table selection for the user to select from.
        -> df.loc[-1] = 'select': adding 'select' as the first row to the dataframe
        ->df.index = df.index + 1:correcting the index
        ->df = df.sort_index(): Sorting the index.
        ->option : type is str, displays the table selection
        ->data1: type is str, loads the read_data()

        --------------------
        Returns
        --------------------
        ->type is str, it returns the table selection menu/dropdown menu

        """


    if st.session_state.CONNECTED:

            cursor = conn.cursor()
            query = ("""select concat(table_schema,'.',table_name) from information_schema.tables
                where table_schema != 'information_schema'
                       AND table_schema != 'pg_catalog' """)

            cursor.execute(query)
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=['data'])
            df.loc[-1] = 'select'
            df.index = df.index + 1
            df = df.sort_index()

            option=st.selectbox('Select table name', df, key='option')
            read_data = read_data()







