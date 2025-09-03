import requests

def aptWX(ICAO):
    url= f"https://aviationweather.gov/api/data/metar?ids={ICAO}&format=raw&taf=true&hours=1"
    try:
        call= requests.get(url=url,timeout= 1.5)
        return (call.text+'******************************************************************\n')
    except Exception as e:
        return [f"{type(e).__name__}: {e}"]