import numpy as np
import math as math 
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astropy.coordinates import FK5
import calendar

input_astronomical_object = input("Enter the name of the astronomical object: ")

input_ra_hours = float(input("Enter the right ascension (Hours): ")) * 15
input_ra_minutes = float(input("Enter the right ascension (Minutes): ")) * 15 / 60
input_ra_seconds = float(input("Enter the right ascension (Seconds): ")) * 15 / 3600
input_ra = input_ra_hours + input_ra_minutes + input_ra_seconds

input_dec_deg = float(input("Enter the declination (Degrees): "))
input_dec_minutes = float(input("Enter the declination (Minutes): ")) / 60
input_dec_seconds = float(input("Enter the declination (Seconds): " )) / 3600
input_dec = input_dec_deg + input_dec_minutes + input_dec_seconds

# Create a SkyCoord object
input_coords = SkyCoord(ra = input_ra, dec = input_dec, unit = 'deg', frame = 'fk5')

# Transform to equatorial coordinates for J2000
input_J2000 = input_coords.transform_to(FK5(equinox='J2000.0'))

# Function to determine the month when the object is highest in the sky
def highest_in_sky_month(ra_deg):
    # Convert RA from degrees to hours
    ra_hours = ra_deg / 15
    # Calculate the month (approximate)
    month = (ra_hours / 2) + 6
    if month > 12:
        month -= 12
    return int(month)

print('-------------------------------------------------')
print(f"Astronomical Object: {input_astronomical_object}")
print(f"Right Ascension (J2000): {input_J2000.ra.deg:.6f} degrees")
print(f"Declination (J2000): {input_J2000.dec.deg:.6f} degrees")

if input_dec < 0:
    print('Southern Hemisphere')
else:
    print('Northern Hemisphere')

# Determine and print the month when the object is highest in the sky
highest_month = highest_in_sky_month(input_J2000.ra.deg)
print(f"The astronomical object will be highest in the sky around month: {calendar.month_name[highest_month]}")

print('-------------------------------------------------')






