import streamlit as st 
from frontend import *
from subject_selection import * 

if "auth" not in st.session_state:
    st.session_state.auth = False 
st.title("Moodle Downloader")

if not st.session_state.auth:
    show_login_form()
if st.session_state.auth:
    sub_links = get_links_for_subject(st.session_state.session,st.session_state.home_page_content)
    selected_sub_finale = select_subjects(sub_links)
    each_sub_data = get_subejct_data(st.session_state.session,selected_sub_finale)
    st.write(each_sub_data)





# goto_page = st.sidebar.radio("Navigation", ("login", "subject_selection", "download"))






# if goto_page == "login":
#     show_login_form()
#     st.write(goto_page)

# elif goto_page =="subject_selection":
#     if st.session_state.auth:
#         sub_links = get_links_for_subject(st.session_state.session,st.session_state.home_page_content)
#         select_subjects(sub_links)
#         st.write(goto_page)
#     else: 
#         st.warning("You need to login first")
# elif goto_page == "download":
#     if st.session_state.auth:
#         # download_subjects()
#         pass
#     else: 
#         st.warning("You need to login first")
        


