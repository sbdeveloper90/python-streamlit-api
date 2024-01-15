import streamlit as st
import streamlit.components.v1 as components
import requests as rq
import urllib.parse
import pandas as pd

import openmeteo_requests
import requests_cache
from retry_requests import retry


def get_weather_description(code: int) -> str:
    """
    Returns the weather description string based on the code parameter.
    """
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Drizzle: Light intensity",
        53: "Drizzle: Moderate intensity",
        55: "Drizzle: Dense intensity",
        56: "Freezing Drizzle: Light intensity",
        57: "Freezing Drizzle: Dense intensity",
        61: "Rain: Slight intensity",
        63: "Rain: Moderate intensity",
        65: "Rain: Heavy intensity",
        66: "Freezing Rain: Light intensity",
        67: "Freezing Rain: Heavy intensity",
        71: "Snow fall: Slight intensity",
        73: "Snow fall: Moderate intensity",
        75: "Snow fall: Heavy intensity",
        77: "Snow grains",
        80: "Rain showers: Slight intensity",
        81: "Rain showers: Moderate intensity",
        82: "Rain showers: Violent intensity",
        85: "Snow showers: Slight intensity",
        86: "Snow showers: Heavy intensity",
        95: "Thunderstorm: Slight or moderate",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    return weather_codes.get(code, "Invalid code")

def degToCompass(num):
    val = int((num / 22.5) + .5)
    arr = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return arr[(val % 16)]


st.set_page_config(
    page_title='Python • Streamlit | API',
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
    st.info("In this example it's used Python Requests with 🌤 [**Open-Meteo Weather API**](https://github.com/open-meteo/open-meteo) to find geocoding location and current meteo forecast.")
    st.success("Find more [**here**](https://open-meteo.com/en/docs/)", icon="↗️")
    st.success("License [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/)", icon="↗️")
    st.warning("The involved APIs are **only** used for testing and showing Streamlit features.")


st.title(":green[Python API Form Calls]")
st.subheader("Fill all the fields in above form box for retrieving weather information of the specific location.")
st.text("The app is using OpenMeteo API for Non-Commercial use, it's only for fun!")
st.divider()


st.title("Location Finder")
with st.form(key='location_form'):
    location = st.text_input('Enter a location:')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    if location != "":
        encoded_location = urllib.parse.quote(location)
        weather_api_call = rq.get(f'https://geocoding-api.open-meteo.com/v1/search?name={encoded_location}&count=1&language=it&format=json')
        if weather_api_call.status_code == 200:
            weather_json = weather_api_call.json()
            st.info(f"Meteo response for **{location}**", icon="ℹ️")
            st.info(f"Location at latitude: **{weather_json['results'][0]['latitude']}** and longitude: **{weather_json['results'][0]['longitude']}**", icon="ℹ️")


            ## Setup the Open-Meteo API client with cache and retry on error
            cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
            retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
            openmeteo = openmeteo_requests.Client(session = retry_session)

            ## Make sure all required weather variables are listed here
            ## The order of variables in hourly or daily is important to assign them correctly below
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": weather_json['results'][0]['latitude'],
                "longitude": weather_json['results'][0]['longitude'],
                "current": ["temperature_2m", "relative_humidity_2m", "is_day", "precipitation", "rain", "snowfall", "weather_code", "wind_speed_10m", "wind_direction_10m"],
                "timezone": "Europe/Berlin",
                "forecast_days": 1
            }
            responses = openmeteo.weather_api(url, params=params)

            ## Process first location. Add a for-loop for multiple locations or weather models
            response = responses[0]
            # print(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
            # print(f"Elevation {response.Elevation()} m asl")
            # print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
            # print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

            ## Current values. The order of variables needs to be the same as requested.
            current = response.Current()
            current_temperature_2m = current.Variables(0).Value()
            current_relative_humidity_2m = current.Variables(1).Value()
            current_is_day = current.Variables(2).Value()
            current_precipitation = current.Variables(3).Value()
            current_rain = current.Variables(4).Value()
            current_snowfall = current.Variables(5).Value()
            current_weather_code = current.Variables(6).Value()
            current_wind_speed_10m = current.Variables(7).Value()
            current_wind_direction_10m = current.Variables(8).Value()
            # print(f"Current time {current.Time()}")

            
            meteo_df = pd.DataFrame({'Temperature (°C)': [current_temperature_2m], 'Relative Humidity (%)': [current_relative_humidity_2m], 'Weather Description': [get_weather_description(current_weather_code)], 'Wind Speed (km/h)': [current_wind_speed_10m], 'Wind Direction': [degToCompass(current_wind_direction_10m)], 'Elevation (m asl)': [response.Elevation()]})
            st.dataframe(meteo_df, hide_index=True)

            map_df = pd.DataFrame({'lat': [weather_json['results'][0]['latitude']], 'lon': [weather_json['results'][0]['longitude']]})
            st.map(map_df, size=300, zoom=10)
        else:
            st.warning("Error retrieving LOCATION information.", icon="⚠️")
    else:
        st.warning("Please fill input field.", icon="⚠️")