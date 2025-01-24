import numpy as np
import math as math
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astropy.coordinates import FK5

# Define RA variables
RA_h = 6
RA_m = 45
RA_s = float(8.9)

# Define declination variables
Dec_d = -16                    
Dec_m = 42
Dec_s = 58

# Convert to degrees
RA_decimal = 15 * (RA_h + RA_m/60 + RA_s/3600)

# Convert to degrees
if Dec_d < 0:
    Dec_decimal = Dec_d - Dec_m/60 - Dec_s/3600
else:
    Dec_decimal = Dec_d + Dec_m/60 + Dec_s/3600
    
# Print out results
print('RA (J2000)  = {:.6f} degrees'.format(RA_decimal))
print('Dec (J2000) = {:.6f} degrees'.format(Dec_decimal))

# Verify with SkyCoord
coord = SkyCoord('6h45m08.9s', '-16d42m58s')
coord