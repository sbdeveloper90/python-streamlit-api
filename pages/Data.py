import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


st.set_page_config(
    page_title='Python • Streamlit | Data',
    page_icon=":sparkles:",
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/sbdeveloper90/python-streamlit-api/wiki',
        'Report a bug': "https://github.com/sbdeveloper90/python-streamlit-api/issues",
        'About': "# Python • Streamlit\n### This is an *extremely* cool app!"
    }
)

with st.sidebar:
    st.title("Credits")
    st.info('Tomassetti, Laura; Torre, Marco; Tratzi, Patrizio; Paolini, Valerio; Rizza, Valeria; Segreto, Marco; Petracchini, Francesco (2020), “Dataset for "Evaluation of air quality and mobility policies in 14 large Italian cities from 2006 to 2016"”, Mendeley Data, V1, doi: 10.17632/n47ddcz9nr.1')
    st.success("Find more [**here**](https://data.mendeley.com/datasets/n47ddcz9nr/1)", icon="↗️")
    st.success("License [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/)", icon="↗️")
    st.warning("The involved datasets are **only** used for testing and showing Streamlit features.")


st.title(":green[Streamlit Data Visualization & Plotting Charts]")
st.subheader('Dataset for "Evaluation of air quality and mobility policies in 14 large Italian cities from 2006 to 2016"')
st.markdown("#")
st.text("Published: 17 April 2020 | Version 1 | DOI: 10.17632/n47ddcz9nr.1")
st.text("Contributors: Laura Tomassetti, Marco Torre, Patrizio Tratzi, Valerio Paolini, Valeria Rizza, Marco Segreto, Francesco Petracchini")
st.divider()

st.markdown("### Description")
st.markdown("Data on air quality and mobility in the 14 Italian metropolitan cities from 2006 to 2016. The cities are: Bari, Bologna, Cagliari, Florence, Genoa, Messina, Milan, Naples, Palermo, Reggio Calabria, Rome, Turin and Venice.")
st.markdown("For each year and each city, air quality data are: concentration and exceedances of NO2, PM10 and PM2.5 in traffic and background monitoring stations.")
st.markdown("For each year and each city, mobility data are: the number of vehicles, motorbikes, trucks and tractors, divided by environmental classification (*i.e. Euro 0, Euro 1, Euro 2, Euro 3, Euro 4, Euro 5, Euro 6*) and by fuel type (*i.e. petrol, gasoil, liquified petroleum gas LPG, compressed natural gas CNG, hybrid and electric cars*); public transport offer and demand, divided by type (*i.e. wheel, rail and water*).")
st.markdown("The number of inhabitants and the municipality surface are also provided for each year and each city.")
st.divider()