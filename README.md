# python-streamlit-api
Python Streamlit example app for API calls and data visualization.



### Useful Links
- [Stremlit Emoji Shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
- [Streamlit Hello World Script](https://github.com/streamlit/hello)
- [Pandas Dataframe Query](https://sparkbyexamples.com/pandas/pandas-dataframe-query-examples/)
- [Pandas Dataframe Filter](https://sparkbyexamples.com/pandas/pandas-dataframe-filter/)

### Docs
- [Streamlit Docs](https://docs.streamlit.io/)
- [Pandas Docs](https://pandas.pydata.org/docs/reference/index.html#api)
- [Python API Docs](https://realpython.com/python-api/)
- [LaTeX Supported Functions](https://katex.org/docs/supported.html)

### Datasets
- [Google Dataset Search](https://datasetsearch.research.google.com/)

### Video Tutorials
- [Streamlit Elements You Should Know About in 2023](https://www.youtube.com/watch?v=_Um12_OlGgw)
- [How to convert a 2D vector logo into 3D](https://www.youtube.com/watch?v=cJTn9P8ltKY)
- [Convert a 2D image to a perfect 3D character model](https://www.youtube.com/watch?v=gJ8Lg3KYkbI&t=2s)
- [Streamlit & Google Sheets: The Easiest "Database"](https://www.youtube.com/watch?v=HwxrXnYVIlU)


<br><hr><br>

```python
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
```

```python
response = rq.get("https://api.example.com")
if response.status_code == 200:
    prPurple("----------- JSON -----------")
    print(response.json())
else:
    match response.status_code:
        case 201:
            prPurple("----------- STATUS CODE -----------")
            prRed("Code " + str(response.status_code) + ": Created")
            prPurple("----------- HEADERS -----------")
            print(response.headers)
        case 400:
            prPurple("----------- STATUS CODE -----------")
            prRed("Code " + str(response.status_code) + ": Bad Request")
            prPurple("----------- HEADERS -----------")
            print(response.headers)
        case 401:
            prPurple("----------- STATUS CODE -----------")
            prRed("Code " + str(response.status_code) + ": Unauthorized")
            prPurple("----------- HEADERS -----------")
            print(response.headers)
        case 404:
            prPurple("----------- STATUS CODE -----------")
            prRed("Code " + str(response.status_code) + ": Not Found")
            prPurple("----------- HEADERS -----------")
            print(response.headers)
        case 405:
            prPurple("----------- STATUS CODE -----------")
            prRed("Code " + str(response.status_code) + ": Method Not Allowed")
            prPurple("----------- HEADERS -----------")
            print(response.headers)
        case 500:
            prPurple("----------- STATUS CODE -----------")
            prRed("Code " + str(response.status_code) + ": Internal Server Error")
            prPurple("----------- HEADERS -----------")
            print(response.headers)
        case _:
            prPurple("----------- STATUS CODE -----------")
            prRed("Code " + response.status_code)
```

```python
f = open('filedidati.json')
data = json.load(f)
f.close()
dataJSON = pd.DataFrame(data['results'])
st.help(dataJSON)
```

```python
codice_zona_unique = dataJSON['codice_zona'].unique()
filtered_df = dataJSON.query("codice_zona == 'quartiere_san_donato'").filter(items=['giorno', 'ora', 'affollamento_medio'])
filtered_df['combined_date'] = filtered_df['giorno'] + "-" + filtered_df['ora'].astype(str)
st.dataframe(data=dataJSON)
st.dataframe(data=dataJSON['geo_point_2d'].values[:1])
st.dataframe(data=codice_zona_unique)
st.dataframe(data=filtered_df)
st.line_chart(data=filtered_df, x='combined_date', y='affollamento_medio')
```

```python
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
```