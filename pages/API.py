import streamlit as st
import streamlit.components.v1 as components
import requests as rq
import json
import pandas as pd
import numpy as np


st.set_page_config(
    page_title='Python • Streamlit | API',
    page_icon=":sparkles:",
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/sbdeveloper90/python-streamlit-api/wiki',
        'Report a bug': "https://github.com/sbdeveloper90/python-streamlit-api/issues",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)