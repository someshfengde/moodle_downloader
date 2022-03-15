import streamlit as st 
from frontend import *
from subject_selection import * 
from zipfile import ZipFile
import os
import shutil


st.set_page_config(
     page_title="Moodle Downloader",
     page_icon="⏬",
     layout="wide",
     initial_sidebar_state="expanded",
 )

is_avail = False 
if "auth" not in st.session_state:
    st.session_state.auth = False 
st.title("Moodle Downloader")
st.write("This application will allow you to select your course and download syllabus files.")
if not st.session_state.auth:
    show_login_form()
if st.session_state.auth:
    sub_links = get_links_for_subject(st.session_state.session,st.session_state.home_page_content)
    selected_sub_finale = select_subjects(sub_links)
    each_sub_data = get_subejct_data(st.session_state.session,selected_sub_finale)
    # st.write(each_sub_data)
    if not os.path.exists("./sample.zip"):
        shutil.make_archive("sample", 'zip', "./")
    zipObj = ZipFile('sample.zip', 'w')

    for course_name , course_title in stqdm(each_sub_data.items()):
        os.mkdir(course_name)
        for label,url in stqdm(course_title.items()):
            save_dir = f"{course_name}/{label}"
            try: 
                r = st.session_state.session.get(url)
                with open(save_dir + ".pdf", 'wb') as f:
                    f.write(r.content)
                    print("pdf_write_written_sucessfully")
                
                zipObj.write(save_dir + ".pdf")
                os.remove(save_dir + ".pdf")
            except:
                st.warning(f"error in {label}")
        os.rmdir(course_name)
        print("\n")
        is_avail = True
    zipObj.close()

    if is_avail:
        with open("sample.zip", "rb") as fp:
            btn = st.download_button(
                label="Download ZIP",
                data=fp,
                file_name="myfile.zip",
                mime="application/zip"
            )
        if btn: 
            st.success("Downloaded Sucessfully")

with st.expander("",expanded = True):
    st.markdown(""" 
    ### About
    This application will help you to download pdf files to your computer from APSIT moodle.
    In this application I've used python streamlit framework to create a web application. 
    This application is developed by [@somesh_fengade](https://www.linkedin.com/in/somesh-9188/)

    I'd like to thank [@jayesh_jain](https://www.linkedin.com/in/jayesh-jain-653a971b8/) 
    and [@prathamesh_hambar](https://www.linkedin.com/in/prathamesh-hambar/) for their help. 

    
    """)

    st.write("""
    ### Repo Link:   
    [![Star]( https://img.shields.io/github/stars/someshfengde/moodle_downloader?style=social)](https://github.com/someshfengde/moodle_downloader)    
    ### Links to my socials:
    [![LinkedIn](https://img.shields.io/github/followers/someshfengde?style=social)](https://github.com/someshfengde)  
    [![](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/somesh-9188/)   
    [![](https://img.shields.io/twitter/follow/someshfengde?style=social)](https://twitter.com/someshfengde)""") 
    st.write("")
    st.write("")

