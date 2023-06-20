from geopy.geocoders import Nominatim
import pytz

# Create a geocoder object
geolocator = Nominatim(user_agent="timezone_finder")

# Prompt the user to enter a place name
place_name = input("Enter a place name: ")

# Perform geocoding to get the location coordinates
location = geolocator.geocode(place_name)

# Check if the location was found
if location is None:
    print("Location not found.")
else:
    # Get the timezone information for the location
    timezone = pytz.timezone(location.timezone)

    # Display the timezone information
    print(f"The timezone for {place_name} is {timezone}")
