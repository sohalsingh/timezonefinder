# timezonefinder

This program allows you to find the timezone of a specific location based on its place name. It utilizes the Geopy library for geocoding and the Pytz library for timezone information.

## Requirements

- Python 3.x
- Geopy library (`pip install geopy`)
- Pytz library (`pip install pytz`)
- Iso3166 library (`pip install iso3166`)

## Usage

1. Run the script `timezonefinder.py`.
2. Enter a place name when prompted.
3. The program will attempt to find the timezone information for the specified location.
4. The timezone information will be displayed if found, otherwise appropriate messages will be shown.

## Example

```
Enter a place name: India
The timezone for India is Asia/Kolkata

```

```
Enter a place name: Unknown Place
Location not found.
```

## Notes

- The program uses the Nominatim geocoder to perform geocoding and retrieve location information based on the place name provided.
- The ISO3166 library is used to find the ISO country code based on the country name extracted from the geocoded location.
- The Pytz library provides timezone information based on the ISO country code.

---

Feel free to customize the README file further based on your specific requirements.

Let me know if you need any further assistance!
