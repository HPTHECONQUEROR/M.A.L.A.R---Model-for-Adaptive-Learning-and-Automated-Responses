import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from datetime import datetime
from geopy.geocoders import Nominatim

class WeatherAnalyzer:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.current_time = self.get_current_time()

        self.cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        self.retry_session = retry(self.cache_session, retries=5, backoff_factor=0.2)
        self.openmeteo = openmeteo_requests.Client(session=self.retry_session)

    def get_current_time(self):
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return int(current_date_time[11:13])

    def get_location_details(self):
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.reverse((self.latitude, self.longitude), language='en')
        return location.address if location else "Location details not available."

    def get_hourly_temperature(self):
        try:
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "hourly": "temperature_2m"
            }
            responses = self.openmeteo.weather_api(url, params=params)
            response = responses[0]
            hourly = response.Hourly()
            return hourly.Variables(0).ValuesAsNumpy(), hourly
        except Exception as e:
            return None, None

    def create_hourly_dataframe(self, hourly_temperature_2m, hourly):
        try:
            hourly_data = {"date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s"),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            ), "temperature_2m": hourly_temperature_2m}
            return pd.DataFrame(data=hourly_data)
        except Exception as e:
            return pd.DataFrame()

    def analyze_weather(self, temperature):
        try:
            if temperature < 15:
                return " It's cold outside"
            elif 15 <= temperature < 25:
                return " The weather is moderate"
            else:
                return " It's hot outside"
        except Exception as e:
            return "with a normal weather outside"

    def greet_user(self):
        try:
            if 0 < self.current_time < 12:
                return "Good morning"
            elif 12 <= self.current_time < 17:
                return "Good afternoon"
            elif 17 <= self.current_time < 20:
                return "Good evening"
            else:
                return "Good night"
        except Exception as e:
            return "Good day"

    def run_analysis(self,Name):
        try:
            hourly_temperature_2m, hourly = self.get_hourly_temperature()
            if hourly_temperature_2m is None or hourly is None:
                raise Exception("Failed to retrieve weather data.")

            hourly_dataframe = self.create_hourly_dataframe(hourly_temperature_2m, hourly)
            if hourly_dataframe.empty:
                raise Exception("Failed to create hourly dataframe.")

            current_temperature = hourly_dataframe[hourly_dataframe['date'] == pd.to_datetime(datetime.now().strftime("%Y-%m-%d %H:00:00"))]['temperature_2m'].values[0]

            greeting = self.greet_user()
            weather_summary = self.analyze_weather(current_temperature)
            location_details = self.get_location_details()
            location_details = location_details.split(',')
            exact_location = f"{location_details[0]}, {location_details[-4]}"
            current_temperature = round(float(current_temperature), 1)

            if greeting == "Good morning":
                return f"Hello {Name}, {greeting} Today's date is {datetime.now().strftime('%d %b %Y')} {weather_summary} with a temperature of {round(current_temperature, 1)} degree Celsius in {exact_location}."
            else:
                return  f"Hello {Name}, {greeting} {weather_summary} with a temperature of {current_temperature} degree Celsius in {exact_location}."
        except Exception as e:
            return f"Hello {Name},. Today's date is {datetime.now().strftime('%d %b %Y')} with a normal weather outside with a temperature of 27 degree Celsius in your location."


if __name__ == "__main__":
    # Usage
    weather_analyzer = WeatherAnalyzer(latitude=17.912540318146725, longitude=9.307831386768845)
    print(weather_analyzer.run_analysis())
    #17.912540318146725, 9.307831386768845