import streamlit  as st 
import numpy as np 
import requests
from stuff_downloader import * 
import streamlit_authenticator as stauth
import gspread

import pandas as pd


from oauth2client.service_account import ServiceAccountCredentials
from tqdm import tqdm


def get_gsheets():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('./resume-sender-339315-4974b1a5a485.json', scope)
    # authorize the clientsheet 
    client = gspread.authorize(creds)
    sheet = client.open('Moodle Downloader')
    sheet_instance = sheet.get_worksheet(0)
    records_data = sheet_instance.get_all_records()
    records_df = pd.DataFrame.from_dict(records_data)
    return records_df, sheet_instance

st.title("Moodle Downloader")

records_df , sheet_instance = get_gsheets()


st.dataframe(records_df)


names = ['John Smith','Rebecca Briggs']
usernames = ['jsmith','rbriggs']
passwords = ['123','456']

hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)

name, authentication_status = authenticator.login('Login','main')