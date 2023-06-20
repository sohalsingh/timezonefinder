from geopy.geocoders import Nominatim
import pytz
from iso3166 import countries


# Create a geocoder object
geolocator = Nominatim(user_agent="timezone_finder")

# Prompt the user to enter a place name
place_name = input("Enter a place name: ")

# Perform geocoding to get the location information
location = geolocator.geocode(place_name, exactly_one=True)

# Check if the location was found
if location is None:
    print("Location not found.")
else:
    # Get the country information
    country_name = location.raw.get('display_name', '').split(',')[-1].strip()

    # Find the ISO country code
    country_code = None
    for country in countries:
        if country_name.lower() == country.name.lower():
            country_code = country.alpha2
            break

    if country_code is None:
        print("Country code not found for the specified location.")
    else:
        # Find the timezone for the country
        try:
            timezone = pytz.country_timezones(country_code)[0]
            print(f"The timezone for {place_name} is {timezone}")
        except IndexError:
            print("Timezone not found for the specified location.")
