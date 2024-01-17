import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt


def filter_data(df):
    # Get column names
    columns = df.columns.tolist()

    # Select columns to filter
    selected_columns = st.multiselect("Select columns to filter", columns)

    # Filter data
    if selected_columns:
        for column in selected_columns:
            filter_value = st.text_input(f"Enter filter value for {column}")
            if filter_value:
                df = df[df[column].astype('string').str.contains(filter_value)]
    return df

def plot_data(df):
    # Get column names
    columns = df.columns.tolist()
    
    # Select columns to plot
    selected_columns = st.multiselect("Select columns to plot (*first one is the x-axis and the second one is the y-axis*)", columns)
    if len(selected_columns) > 1:
        # Plot data
        if selected_columns:
            chart_type = st.selectbox("Select chart type", ["Line Chart", "Bar Chart"])
            if chart_type == "Line Chart":
                chart = alt.Chart(df).mark_line(point={'filled': False, 'fill': 'white', 'size': 50}).encode(
                    x=selected_columns[0],
                    y=selected_columns[1]
                ).interactive()
            elif chart_type == "Bar Chart":
                chart = alt.Chart(df).mark_bar().encode(
                    x=selected_columns[0],
                    y=selected_columns[1]
                ).interactive()

            st.altair_chart(chart, use_container_width=True)


st.set_page_config(
    page_title='Python • Streamlit | File',
    page_icon=":sparkles:",
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/sbdeveloper90/python-streamlit-api/wiki',
        'Report a bug': "https://github.com/sbdeveloper90/python-streamlit-api/issues",
        'About': "# Python • Streamlit\n### This is an *extremely* cool app!"
    }
)

st.title(":green[Streamlit Data Visualization & Plotting Charts - from Uploaded File]")
st.subheader("This section of the app allows to upload *.xlsx* or *.csv* file, analize and plot it.")
st.divider()


st.title(":red[Data Analysis with Streamlit]")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "csv"])
st.warning('Pay attention to the ti data type of the cells in the loaded excel files, if not correct it could create problems in serializing the dataframes', icon='⚠️')

if uploaded_file is not None:
    # Read data
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(".xlsx") else pd.read_csv(uploaded_file)

    # Display data
    st.subheader(":red[Data]")
    st.dataframe(df, use_container_width=True)

    # Filter data
    st.subheader(":red[Filtered Data]")
    filtered_df = filter_data(df)
    st.dataframe(filtered_df)

    # Plot data
    st.subheader(":red[Plots Filtered Data]")
    plot_data(filtered_df)