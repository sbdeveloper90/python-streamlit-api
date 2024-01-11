import streamlit as st
import streamlit.components.v1 as components
import requests as rq
import urllib.parse
from ansi2html import Ansi2HTMLConverter


st.set_page_config(
    page_title='Python • Streamlit | API',
    page_icon=":sparkles:",
    layout='centered',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/sbdeveloper90/python-streamlit-api/wiki',
        'Report a bug': "https://github.com/sbdeveloper90/python-streamlit-api/issues",
        'About': "# Python • Streamlit\n### This is an *extremely* cool app!"
    }
)


st.title(':green[Python API Form Calls]')
st.subheader("Fill all the fields in above form box")
st.divider()


st.title("Location Finder")
with st.form(key='location_form'):
    location = st.text_input('Enter a location:')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    encoded_location = urllib.parse.quote(location)
    weather_api_call = rq.get(f"https://wttr.in/{encoded_location}")
    # weather_api_call = rq.get(f"https://wttr.in/{encoded_location}?format=%C\n%t\n%h\n%w\n%l\n")
    # st.map(latitude=37.7749, longitude=-122.4194)
    if weather_api_call.status_code == 200:
        # weather_info = weather_api_call.text.split("\n")
        # city = weather_info[0]
        # temperature = weather_info[1]
        # humidity = weather_info[2]
        # wind = weather_info[3]
        # print(f"The weather in {city} is {temperature} and {humidity} humid with wind speeds of {wind}.")
        
        conv = Ansi2HTMLConverter()
        html = conv.convert(weather_api_call.text)
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.text("Error retrieving weather information.")