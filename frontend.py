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




st.title("Moodle Downloader")
records_df , sheet_instance = get_gsheets()
st.dataframe(records_df)

username = st.sidebar.text_input("User Name")
password = st.sidebar.text_input("Password",type='password')

def login_me(username , password):
    payload = {
        "username": username,
        "password": password,
        "rememberusername": 1,
        "anchor": None
    }
    s,r = get_session(payload)
    return s,r

if st.sidebar.button("Login"):
    s,r = login_me(username,password)
    if check_auth(r):
        subjects_and_links = get_links_for_subject(s,r)
        selected_keys = [] 
        for x in subjects_and_links.keys():
            selected_keys =  st.checkbox(x,selected_keys) 
        known_variables = {selected_link: st.checkbox(f"{subject} ({selected_link})") for subject, selected_link in subjects_and_links}  

        st.write(known_variables)
        # options = st.multiselect("Choose subjects to download", subjects_and_links.keys())
        # st.write("selected subjects are : ",options)

        # st.write(subjects_and_links)

    # if password == '12345':
    # create_usertable()
    # hashed_pswd = make_hashes(password)

    # st.success("Logged In as {}".format(username))

    # task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
    # if task == "Add Post":
    #         st.subheader("Add Your Post")

    #     elif task == "Analytics":
    #         st.subheader("Analytics")
    #     elif task == "Profiles":
    #         st.subheader("User Profiles")
    #         user_result = view_all_users()
    #         clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
    #         st.dataframe(clean_db)
else :
    st.warning("Incorrect Username/Password")
# names = ['John Smith','Rebecca Briggs']
# usernames = ['jsmith','rbriggs']
# passwords = ['123','456']

# hashed_passwords = stauth.hasher(passwords).generate()

# authenticator = stauth.authenticate(names,usernames,hashed_passwords,
#     'some_cookie_name','some_signature_key',cookie_expiry_days=30)

# name, authentication_status = authenticator.login('Login','main')