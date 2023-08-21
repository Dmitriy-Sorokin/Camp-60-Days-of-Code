import streamlit as st
import plotly.express as px

import requests

API_KEY = "349a35d3f3c95904257d35da7e26381d"


def get_data(place, forecast_day=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value = 8 * forecast_day
    filtered_data = filtered_data[:nr_value]
    return filtered_data


# Add title, text input, slider, select_box, and sub_header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", max_value=1, min_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Create a temperature plot
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "C:\projects\Camp-60-Days-of-Code\day_32\images\clear.png",
                      "Clouds": "C:\projects\Camp-60-Days-of-Code\day_32\images\cloud.png",
                      "Rain": "C:\projects\Camp-60-Days-of-Code\day_32\images\rain.png",
                      "Snow": "C:\projects\Camp-60-Days-of-Code\day_32\images\snow.png"}
            images_paths = [images[condition] for condition in sky_condition]
            st.image(images_paths)
    except KeyError:
        st.write("Enter correctly city")
