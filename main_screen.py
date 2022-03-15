import streamlit as st 
from frontend import *
from subject_selection import * 
from zipfile import ZipFile
import os
import shutil


is_avail = False 
if "auth" not in st.session_state:
    st.session_state.auth = False 
st.title("Moodle Downloader")

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

with st.expander("About",expanded = True):
    st.markdown(""" 

    This application will help you to download pdf files to your computer from APSIT moodle.
    In this application I've used python streamlit framework to create a web application. 
    This application is developed by [@somesh_fengade](https://www.linkedin.com/in/somesh-9188/)

    I'd like to thank [@jayesh_jain](https://www.linkedin.com/in/jayesh-jain-653a971b8/) 
    and [@prathamesh_hambar](https://www.linkedin.com/in/prathamesh-hambar/) for their help. 

    links for my socials:


    ![![Follow](<https://img.shields.io/twitter/follow/><username>?style=social)](https://twitter.com/<username>)
    ![](https://raw.githubusercontent.com/hussainweb/hussainweb/main/icons/instagram.png)(<https://www.twitter.com/><username>)
        <a href="https://www.instagram.com/abhishknads/">
        <img align="left" alt="Abhishek's Instagram" width="22px" src="https://raw.githubusercontent.com/hussainweb/hussainweb/main/icons/instagram.png" />
        </a>
        <a href="https://discord.gg/XTW52Kt">
        <img align="left" alt="Abhishek's Discord" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/discord.svg" />
        </a>
        <a href="https://twitter.com/abhisheknaiidu">
        <img align="left" alt="Abhishek Naidu | Twitter" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/twitter.svg" />
        </a>
        <a href="https://www.linkedin.com/in/abhisheknaiidu/">
        <img align="left" alt="Abhishek's LinkedIN" width="22px" src="https://raw.githubusercontent.com/peterthehan/peterthehan/master/assets/linkedin.svg" />
        </a>
    """)
st.write("[![](./github.gif)](https://github.com/someshfengde/moodle_downloader)")
st.write("[![Star](<https://img.shields.io/github/stars/><username>/<repo>.svg?logo=github&style=social)](<https://gitHub.com/><username>/<repo>)")