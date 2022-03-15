from stuff_downloader import * 
from frontend import * 
import streamlit as st 
import numpy as np 

def select_subjects(subjects_and_links):
    """
    Returns a list of subjects to download 
    """
    selected_subjects_finale = {}
    form_samp = st.empty()
    form = form_samp.form("subject_selection")
    selected_subjects = {}
    subjects_and_links = {k:v for k,v in subjects_and_links.items() if v is not None and k is not None}

    for x, y in subjects_and_links.items():
        selected_subjects[x] = form.checkbox(x)
    submitted = form.form_submit_button("Submit")
    if submitted:
        for x, y in selected_subjects.items():
            if y:
                selected_subjects_finale[x] = subjects_and_links[x]
        st.success(f"You have selected {len(selected_subjects_finale)} subjects")
        form_samp.empty()
        # download_subjects(selected_subjects_finale)

    # st.write(selected_subjects_finale)
    return selected_subjects_finale