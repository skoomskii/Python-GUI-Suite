import os
from datetime import datetime
from geopy.geocoders import Nominatim
import openmeteo_requests
import requests_cache
from retry_requests import retry

def getloc(address):
    geolocator = Nominatim(user_agent="WXFetch")
    geoloc = geolocator.geocode(f"{address}")
    location = [geoloc.address,geoloc.latitude,geoloc.longitude]
    return location

def getWX(loc, lat, lon):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "is_day", "precipitation", "cloud_cover", "pressure_msl", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m", "rain", "showers", "snowfall"],
        "timezone": "auto",
        "timeformat": "unixtime"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    current = response.Current()
    Location = f"Location: {loc}"
    Coordinates = f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E"
    Elevation = f"Elevation (ASL): {response.Elevation()} m"
    Timezone = f"Timezone: {response.TimezoneAbbreviation()}".replace("b","")
    Offset = f"GMT Offset: {response.UtcOffsetSeconds()} s"
    Time = f"Time: {datetime.fromtimestamp(current.Time())} hrs"

    # Current values. The order of variables needs to be the same as requested.
    current_temperature_2m = f"Temperature: {round(current.Variables(0).Value())}°C"
    current_relative_humidity_2m = f"Relative Humidity: {current.Variables(1).Value()} %"
    current_is_day = f"Day Light: {current.Variables(2).Value()}"
    current_precipitation = f"Precipitation: {current.Variables(3).Value()} mm"
    current_cloud_cover = f"Cloud Cover: {current.Variables(4).Value()} %"
    current_pressure_msl = f"Pressure (MSL): {round(current.Variables(5).Value())} hPa"
    current_wind_speed_10m = f"Wind Speed: {round(current.Variables(6).Value())} km/h"
    current_wind_direction_10m = f"Wind Direction: {round((current.Variables(7).Value()))}°"
    current_wind_gusts_10m = f"Wind Gusts: {round((current.Variables(8).Value()))} km/h"
    current_rain = f"Rain: {current.Variables(9).Value()} mm"
    current_showers = f"Showers: {current.Variables(10).Value()} mm"
    current_snowfall = f"Snowfall: {current.Variables(11).Value()} m"

    print("******************** Current Weather ********************")

    return f"{Location},{Coordinates},{Elevation},{Timezone},{Offset},{Time},{current_temperature_2m},{current_relative_humidity_2m},{current_is_day},{current_precipitation},{current_cloud_cover},{current_pressure_msl},{current_wind_speed_10m},{current_wind_direction_10m},{current_wind_gusts_10m},{current_rain},{current_showers},{current_snowfall}\n"

def display(data):
    wx = data.split(',')
    for i in wx:
        print(i)
    print("************************************************************")

def getLog(location):
    wx = []
    if (os.path.exists('wxlog.txt')):
        with open('wxlog.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            i = len(data)-1
            while (i >= 0):
                if location in data[i]:
                    wx = data[i]
                    break
                i -= 1
            file.closed
            if (len(wx) == 0): return None
            else: return wx
        True
    else : return None

def wxLog(data):
    with open('wxlog.txt', 'a', encoding='utf-8') as file:
        file.writelines(data)
        file.closed
        print('********************** Weather Logged **********************')
    True

def fetch(add,lat,lon):
    os.system('cls')
    wx = getWX(add,lat,lon)
    display(wx)
    wxLog(wx)
    clr = input('Clear:')
    if (len(clr) > 0):
        os.system('cls')
        main()

def main():
    try:
        print("********************** Weather Fetcher **********************")
        location = input('Location: ')
        latlon = getloc(str(location))
        log = getLog(str(latlon[0]))
        if (log == None): fetch(latlon[0],latlon[1],latlon[2])
        else: 
            os.system('cls')
            print("********************** Logged Weather **********************")
            display(log)
            update = input('Update: ')
            if (len(update) > 0): fetch(latlon[0],latlon[1],latlon[2])
    except:
        print('******************* Connection Failed *******************')
        refresh = input('Refresh: ')
        if (len(refresh) > 0):
            os.system('cls')
            main()
main()