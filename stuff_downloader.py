#%%
import re as re
import requests 
import bs4 as bs4
from tqdm import tqdm 
import requests
import time
import streamlit  as st 
import numpy as np 
import requests
from stuff_downloader import * 
import streamlit_authenticator as stauth
from bs4 import BeautifulSoup
import gspread
import pandas as pd
from stqdm import stqdm
import os 
from oauth2client.service_account import ServiceAccountCredentials
from tqdm import tqdm





def create_keyfile_dict():
    variables_keys = {
        "type": os.environ["type"],
        "project_id": os.environ["project_id"],
        "private_key_id": os.environ["private_key_id"],
        "private_key": os.environ["private_key"],
        "client_email": os.environ["client_email"],
        "client_id": os.environ["client_id"],
        "auth_uri": os.environ["auth_uri"],
        "token_uri": os.environ["token_uri"],
        "auth_provider_x509_cert_url": os.environ["auth_provider_x509_cert_url"],
        "client_x509_cert_url": os.environ["client_x509_cert_url"]
    }
    return variables_keys

def get_session(payload):
    """
    Returns a requests.session and response 
    """
    url = "http://moodle.apsit.org.in/moodle/login/index.php"
    s = requests.session()
    r = s.post(url, data=payload)
    return s,r 

def get_gsheets():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_dict(create_keyfile_dict(), scope)
    # authorize the clientsheet 
    client = gspread.authorize(creds)
    sheet = client.open('Moodle Downloader')
    sheet_instance = sheet.get_worksheet(0)
    # records_data = sheet_instance.get_all_records()
    # records_df = pd.DataFrame.from_dict(records_data)
    return sheet_instance



def check_auth(r):
    """
    checks if the user is authenticated or not 
    """
    soup = bs4.BeautifulSoup(r.content,'html.parser')
    region_1 = soup.find_all("div", {"class": "loginerrors"})
    region_2 = soup.find_all("div", {"class": "box errorbox"})
    if len(region_2) or len(region_1):
        st.error("Please try to login again, incorrect login or password")
        return False
    else: 
        st.success("Authenticated")
        return True
        

def get_links_for_subject(session,home_page_content,return_total_links= False ):
    """
    returns the links to the subjects
    """
    subjects_and_links = {}
    soup = bs4.BeautifulSoup(home_page_content.content,'html.parser')
    total_links = soup.find_all('a', href=True)
    for link in soup.find_all('a', attrs={'href': re.compile("^http://moodle.apsit.org.in/moodle/course/view")}):
        subjects_and_links[link.get("title")] = link.get('href')
    
    if return_total_links:
        return subjects_and_links,total_links
    else:
        return subjects_and_links   

def get_subejct_data(session , subject_links, return_all_subjects = True, return_in_folder_files = False, subject_url= None):
    """


    returns the data of the subject
    if returns_all_subjects:
        this requires dictionary format for the links to subject and subject name 
        returns the links to all the subjects
    if return_in_folder_files:
        counts and collects links to the files inside folders too. 
    
    if return_all_subject is false: 
        specify the parameter subject_url and you will be getting links to that subjects particularly 
    """
    if return_all_subjects:
        subject_wise_links = {}
        count =0 
        for title, urls in stqdm(subject_links.items()):
            
            subject_wise_links[title] = {}
            r = session.get(urls)
            soup = bs4.BeautifulSoup(r.content,'html.parser')
            try:
                for link in stqdm(soup.find_all('a', attrs={'href': re.compile("^http://moodle.apsit.org.in/moodle/mod/resource/view")})):
                    subject_wise_links[title][link.span.text] = link.get('href')
                
                if return_in_folder_files:
                    for link in soup.find_all('a', attrs={'href': re.compile("^http://moodle.apsit.org.in/moodle/mod/folder/view")}):
                        another_r = session.get(link.get('href'))
                        another_soup = bs4.BeautifulSoup(another_r.content,'html.parser')
                        for another_link in another_soup.find_all('a', attrs={'href': re.compile("^http://moodle.apsit.org.in/moodle/mod/resource/view")}):
                            subject_wise_links[title][another_link.span.text] = another_link.get('href')
                        # subject_wise_links[title][link.span.text] = link.get('href')
            except: 
                print("error in subject: ",title)
            # time.sleep(10)
            # count +=1
            # if count ==5 : 
            #     break 
        return subject_wise_links
    else: 
        if subject_url is None:
            raise Exception("Specify the subject url")
        else:
            r = session.get(subject_url)
            soup = bs4.BeautifulSoup(r.content,'html.parser')
            subject_links_arr = {}
            for link in stqdm(soup.find_all('a', attrs={'href': re.compile("^http://moodle.apsit.org.in/moodle/mod/resource/view")})):
                subject_links_arr[link.span.text] = link.get('href')

            if return_in_folder_files:
                for link in stqdm(soup.find_all('a', attrs={'href': re.compile("^http://moodle.apsit.org.in/moodle/mod/folder/view")})):
                    subject_links_arr[link.span.text] = link.get('href')
            
            return subject_links_arr


def filter_pdf_files(links_arr):
    """
    returns the links to the pdf files
    """
    pdf_links = []
    for link in links_arr:
        if link.endswith(".pdf"):
            pdf_links.append(link)
    return pdf_links







