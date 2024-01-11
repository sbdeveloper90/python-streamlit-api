import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title='Python • Streamlit | Home',
    page_icon=":sparkles:",
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/sbdeveloper90/python-streamlit-api/wiki',
        'Report a bug': "https://github.com/sbdeveloper90/python-streamlit-api/issues",
        'About': "# Python • Streamlit\n### This is an *extremely* cool app!"
    }
)

# components.iframe("https://my.spline.design/streamlitlogo-eaa8c1fc0230ef4c8fc84a2b482f4f6d/", height=200)

st.markdown('<h1 style="color:#3DD56D; text-align:center">Python Streamlit API & Data Visualization</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center">Python Streamlit example app for API calls and data visualization</h3>', unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')

st.latex(r'''
    \LARGE(\delta + m)\psi = 0
    ''')

def quiz():
    question = ":shamrock: Who is the author of the showed equation?"
    options = ["Albert Einstein", "Paul Dirac", "Robert Oppenheimer"]
    correct_answer = "Paul Dirac"
    selected_answer = st.radio(question, options)
    if st.button("Answer"):
        if selected_answer == correct_answer:
            st.success("Correct!")
        else:
            st.error("Incorrect. Please try again.")

with st.sidebar:
    quiz()