electromagnetic_radiation = float(input("Enter em: "))
ert = input("what units?")
conversion_type = input("what would you like to convert to: Frequency, Wavelength, or Energy?")

GHz = 'GHz'
um = 'um'
nm = 'nm'
keV = 'KeV' 
MeV = 'Mev'

def Energy():
    if ert == GHz:
       print(electromagnetic_radiation * (10**9))
    elif ert == um:
        print((2.99792458*10**14) / electromagnetic_radiation)
    elif ert == nm:
        print(electromagnetic_radiation * 2.41799050402417*10**17)
    elif ert == MeV:
        print(electromagnetic_radiation * 2.41799050402417*10**20)

def wavelength():
    if ert == GHz:
       print(electromagnetic_radiation * (10**9))
    elif ert == um:
        print((2.99792458*10**14) / electromagnetic_radiation)
    elif ert == nm:
        print(electromagnetic_radiation * 2.41799050402417*10**17)
    elif ert == MeV:
        print(electromagnetic_radiation * 2.41799050402417*10**20)

def frequency():
    if ert == GHz:
       print(electromagnetic_radiation * (10**9))
    elif ert == um:
        print((2.99792458*10**14) / electromagnetic_radiation)
    elif ert == nm:
        print(electromagnetic_radiation * 2.41799050402417*10**17)
    elif ert == MeV:
        print(electromagnetic_radiation * 2.41799050402417*10**20)

match conversion_type:
    case "Frequency":
        frequency()
    case "Wavelength":
        wavelength()
    case "Energy":
        Energy()
    case _:
        print("Invalid Conversion Type")