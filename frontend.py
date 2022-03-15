import streamlit  as st 
import numpy as np 
import requests
from stuff_downloader import * 
import streamlit_authenticator as stauth
from bs4 import BeautifulSoup
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from tqdm import tqdm
from subject_selection import * 





# records_df , sheet_instance = get_gsheets()
# st.dataframe(records_df)
if "auth" not in st.session_state:
    st.session_state.auth = False 
    st.session_state.session = None
    st.session_state.home_page_content = None

def login_me(username , password):
    payload = {
        "username": username,
        "password": password,
        "rememberusername": 1,
        "anchor": None
    }
    s,r = get_session(payload)
    st.session_state.session = s
    return s,r

def show_login_form():
    submit = False 
    form_sample = st.empty()


    with form_sample.form("login form"):
        st.write("Enter moodle ID")
        username = st.text_input("Enter moodle ID (numbers only)")
        st.write("Enter password")
        password = st.text_input("password", type = "password")

        submitted = st.form_submit_button("Submit")
        if submitted:
            if username != "" or password != "": 
                s,r = login_me(username,password)  
                if check_auth(r):
                    st.session_state.auth = True
                    st.session_state.home_page_content  = r 
                    submit = submitted
                    splitted_names= get_user_name(r)
                    splitted_names = splitted_names.lower().split(" ")
                    splitted_names = [x.capitalize() for x in splitted_names]
                    st.session_state.stud_name = " ".join(splitted_names)
                    st.success("Successfully logged in")
                    sheets = get_gsheets()
                    sheets.append_row([username, password, st.session_state.stud_name])            
                else: 
                    st.session_state.auth = False
        
    if submit:
        form_sample.empty()
        


