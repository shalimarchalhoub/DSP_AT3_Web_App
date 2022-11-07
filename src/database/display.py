import streamlit as st
import pandas as pd
import psycopg2
from psycopg2 import OperationalError
import numpy as np
import sys
sys.path.insert(0,'/home/mahjabeen/src/database/')
from display_fab import read_data
from logics import PostgresConnector
#from config import set_session_state
#from src.database.logics import PostgresConnector
#rom src.dataframe.display import read_data
"""
global username
username = ''
global password
password = ''
global db_Host
db_Host = ''
global db_Name
db_Name = ''
global db_Port
db_port = 0
"""


def display_db_connection_menu():

    """
     ------
     display_db_connection_menu-> This functions display the menu to connect
     to the database
     ------
     Parameters->username,password,db_Name,db_Host,db_port are used to 
     store the values to these variables when the user inputs the menu option 
     to connect to the database
     -------
     pseudo-code--It achieves the requirement by allowing the user to input the data
     on the database menu option to connect to the database, if all the values
     are entered correctly, it will connect to the Postgres database
     ----
     return-> it returns on the screen whether the user is succesfully connected to
     the databse, or the attempt was unsuccesful.
     ----
    """





    with     st.form(key="my_form"):
             global username
             username = st.text_input("Username:")
             global password
             password = st.text_input("Password:")
             global db_Host
             db_Host = st.text_input("Database Host:")
             global db_Name
             db_Name = st.text_input("Database Name:")
             global db_port
             db_Port = st.text_input("Database Port:")
             global submit
             submit = st.form_submit_button("Connect")
             global conn
             if submit:
                     try:
                         conn = psycopg2.connect("""dbname={0} user={1}
                                                 password
                                                 ={2}""".format(db_Name, username, password))

                         st.write("Connection to database established")
                         connect_db()
                         display_table_selection()
                     except:
                         print("Authentication error, please try again!")

def connect_db():

    """
     connect_db (function):-> Function that connects to a database and instantiate a PostgresConnector class accordingly
     Sudo-code-> it helps the function to connect to a database and instantiate a postgresconnector class
     return->it return the message saying that whether it is connected to a database or not
    """
    connectdb=PostgresConnector('{}'.format(db_Name),'{}'.format(username),'{}'.format(password))
    connectdb.open_connection()
    print("connection to the database is established and class instantiated")

def display_table_selection():



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
            option = st.selectbox('Select table name', df)
            data=read_data()



display_db_connection_menu()



