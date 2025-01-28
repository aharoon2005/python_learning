import numpy as np
import math as math

electromagnetic_radiation = float(input("Enter em: "))
ert = input("what units?: ")                                                                            # Input interface to tell the program what you want
conversion_type = input("what would you like to convert to: Frequency, Wavelength, or Energy?: ")

GHz = 'GHz'
um = 'um'
nm = 'nm'                     # Defining variables that will be the inputs for ert (electromagnetic radiation type)
keV = 'keV' 
MeV = 'MeV'

def Energy():
    if ert == GHz:
       print(electromagnetic_radiation * (4.1356*10**-6))
    elif ert == um:
        print(((4.1357*10**-15) * (3*10**8)) / ((electromagnetic_radiation) * 10**-6))
    elif ert == nm:
        print(((4.1357*10**-15) * (3*10**8)) / ((electromagnetic_radiation) * 10**-9))
    elif ert == keV:                                                                      #functions depending on which unit you want to convert
        print(electromagnetic_radiation * 1000)
    elif ert == MeV:
        print(electromagnetic_radiation * 10**6)

def wavelength():
    if ert == GHz:
       print(0.299792458 / electromagnetic_radiation)
    elif ert == um:
        print(electromagnetic_radiation * 10**-6)
    elif ert == nm:
        print(electromagnetic_radiation * 10**-9)
    elif ert == keV:
        print(((4.1357*10**-15) * (3*10**8)) / ((electromagnetic_radiation) * 1000))
    elif ert == MeV:
        print(((4.1357*10**-15) * (3*10**8)) / ((electromagnetic_radiation) * 10**6))

def frequency():
    if ert == GHz:
       print(electromagnetic_radiation * (10**9))
    elif ert == um:
        print((2.99792458*10**14) / electromagnetic_radiation)
    elif ert == nm:
        print((2.99792458*10**17) / electromagnetic_radiation)
    elif ert == keV:
        print(electromagnetic_radiation * 2.418*10**17)
    elif ert == MeV:
        print(electromagnetic_radiation * 2.418*10**20)

match conversion_type:
    case "Frequency":
        frequency()
    case "FREQUENCY":
        frequency()
    case "frequency":
        frequency()
    case "Wavelength":
        wavelength()
    case "WAVELENGTH":
        wavelength()
    case "wavelength":
        wavelength()                                        # Calls each function depending on which conversion type you input
    case "Energy":
        Energy()
    case "ENERGY":
        Energy()
    case "energy":
        Energy()
    case _:
        print("Invalid Conversion Type")