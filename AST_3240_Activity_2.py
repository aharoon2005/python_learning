import numpy as np
import math as math
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astropy.coordinates import FK5

ngp_galactic = SkyCoord(ra = 192.25, dec = 27.4, unit = 'deg', frame = 'fk5')


# Transform to equatorial coordinates for B1950
ngp_B1950 = ngp_galactic.transform_to(FK5(equinox='B1950.0'))

# Transform to equatorial coordinates for J2000
ngp_J2000 = ngp_galactic.transform_to(FK5(equinox='J2000.0'))

# Get declination of the north Galactic pole for both epochs
dec_B1950 = ngp_B1950.dec.deg
dec_J2000 = ngp_J2000.dec.deg

# Print out results
print(f"Declination of the north Galactic pole (B1950): {dec_B1950:.6f} degrees")
print(f"Declination of the north Galactic pole (J2000): {dec_J2000:.6f} degrees")

# Compare declinations
if dec_J2000 > dec_B1950:
    print("The angle between the celestial equator and the Galactic equator is increasing with time.")
elif dec_J2000 < dec_B1950:
    print("The angle between the celestial equator and the Galactic equator is decreasing with time.")
else:
    print("The angle remains constant.")