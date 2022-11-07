import streamlit as st
from PIL import Image
def set_app_config():

    icon = Image.open('/home/mahjabeen/analysis.png')
    st.set_page_config(
    page_title="Streamlit application for performing data exploration on a database",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
            'Get Help': 'https://streamlit.io',
            'Report a bug': 'https://github.com',
            'About':'About your applicatioin: **data exploration on a database***'
            }
    )


def set_session_state(key, value):
