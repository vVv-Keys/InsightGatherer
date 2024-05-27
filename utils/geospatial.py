from geopy.geocoders import Nominatim

def fetch_geolocation(query):
    geolocator = Nominatim(user_agent="osint_tool")
    location = geolocator.geocode(query)
    return {'address': location.address, 'latitude': location.latitude, 'longitude': location.longitude}
