import streamlit as st
import streamlit.components.v1 as components
import requests as rq
import json
import pandas as pd
import numpy as np


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))



# f = open('filedidati.json')
# data = json.load(f)
# f.close()
# dataJSON = pd.DataFrame(data['results'])
# st.help(dataJSON)

st.set_page_config(
    page_title='Data API • Streamlit',
    page_icon=":sparkles:",
    # layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/sbdeveloper90/python-streamlit-api/wiki',
        'Report a bug': "https://github.com/sbdeveloper90/python-streamlit-api/issues",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# st.title(':green[IPERBOLE BolognaWifi Affollamento]')
# st.write("Dati in forma di aggregata relativi all'affollamento orario nelle aree con il WiFi pubblico, dove per affollamento si intende quanti dispositivi sono presenti nell'area ogni ora del giorno")
# st.divider()


st.title('Generatore di URL personalizzati')

# Aggiungi i campi del form
with st.form(key='my_form'):
    name = st.text_input(label='Nome')
    age = st.number_input(label='Età')
    city = st.text_input(label='Città')
    submit_button = st.form_submit_button(label='Genera URL')

# Genera l'URL personalizzato
if submit_button:
    url = f'https://api.example.com?name={name}&age={age}&city={city}'
    st.write(f'Ecco il tuo URL personalizzato: {url}')


# components.iframe("https://my.spline.design/streamlitlogo-eaa8c1fc0230ef4c8fc84a2b482f4f6d/", width=1000, height=1000)


# codice_zona_unique = dataJSON['codice_zona'].unique()
# filtered_df = dataJSON.query("codice_zona == 'quartiere_san_donato'").filter(items=['giorno', 'ora', 'affollamento_medio'])
# filtered_df['combined_date'] = filtered_df['giorno'] + "-" + filtered_df['ora'].astype(str)
# st.dataframe(data=dataJSON)
# st.dataframe(data=dataJSON['geo_point_2d'].values[:1])
# st.dataframe(data=codice_zona_unique)
# st.dataframe(data=filtered_df)
# st.line_chart(data=filtered_df, x='combined_date', y='affollamento_medio')