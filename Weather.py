import urllib.request
import math

def Degree(WindDirComp):
    if 0 <= WindDirection < 5.62:
        WindDirComp = "N (North)"
    elif 5.63 < WindDirection < 16.87:
        WindDirComp = "NbE (North by East)"
    elif 16.88 < WindDirection < 28.12:
        WindDirComp = "NNE (North-Northeast)"
    elif 28.13 < WindDirection < 39.37:
        WindDirComp = "NEbN (Northeast by North)"
    elif 39.38 < WindDirection < 50.62:
        WindDirComp = "NE (Northeast)"
    elif 50.63 < WindDirection < 61.87:
        WindDirComp = "NEbE (Northeast by East)"
    elif 61.88 < WindDirection < 73.12:
        WindDirComp = "ENE (East-Northeast)"
    elif 73.13 < WindDirection < 84.37:
        WindDirComp = "EbN (East by North)"
    elif 84.38 < WindDirection < 95.62:
        WindDirComp = "E (East)"
    elif 95.63 < WindDirection < 106.87:
        WindDirComp = "EbS (East by South)"
    elif 106.88 < WindDirection < 118.12:
        WindDirComp = "ESE (East-Southeast)"
    elif 118.13 < WindDirection < 129.37:
        WindDirComp = "SEbE (Southeast by East)"
    elif 129.38 < WindDirection < 140.62:
        WindDirComp = "SE (Southeast)"
    elif 140.63 < WindDirection < 151.87:
        WindDirComp = "SEbS (Southeast by South)"
    elif 151.88 < WindDirection < 163.12:
        WindDirComp = "SSE (South-Southeast)"
    elif 163.13 < WindDirection < 174.37:
        WindDirComp = "SbE (South by East)"
    elif 174.38 < WindDirection < 185.62:
        WindDirComp = "S (South)"
    elif 185.63 < WindDirection < 196.87:
        WindDirComp = "SbW (South by West)"
    elif 196.88 < WindDirection < 208.12:
        WindDirComp = "SSW (South-Southwest)"
    elif 208.13 < WindDirection < 219.37:
        WindDirComp = "SWbS (Southwest by South)"
    elif 219.38 < WindDirection < 230.62:
        WindDirComp = "SW (Southwest)"
    elif 230.63 < WindDirection < 241.87:
        WindDirComp = "SWbW (Southwest by West)"
    elif 241.88 < WindDirection < 253.12:
        WindDirComp = "WSW (West-Southwest)"
    elif 253.13 < WindDirection < 264.37:
        WindDirComp = "WbS (West by South)"
    elif 264.38 < WindDirection < 275.62:
        WindDirComp = "W (West)"
    elif 275.63 < WindDirection < 286.87:
        WindDirComp = "WbN (West by North)"
    elif 286.88 < WindDirection < 298.12:
        WindDirComp = "WNW (West-Northwest)"
    elif 298.13 < WindDirection < 309.37:
        WindDirComp = "NWbW (Northwest by West)"
    elif 309.38 < WindDirection < 320.62:
        WindDirComp = "NW (Northwest)"
    elif 320.63 < WindDirection < 331.87:
        WindDirComp = "NWbN (Northwest by North)"
    elif 331.88 < WindDirection < 343.12:
        WindDirComp = "NNW (North-Northwest)"
    elif 343.13 < WindDirection < 354.37:
        WindDirComp = "NbW (North by West)"
    elif 354.38 < WindDirection <= 360:
        WindDirComp = "N (North)"
    return WindDirComp

ICAO = input("What airport would you like to find the weather conditions for? (Use ICAO code)")
ICAO = ICAO.upper()

pageText = urllib.request.urlopen('http://w1.weather.gov/data/METAR/' + ICAO + '.1.txt')
pageText = str(pageText.read())

A = pageText[45:]
print(A)
list = A.split()
Airport = list[0]

Day = list[1][0:2]
Hour = list[1][2:4]
Minute = list[1][4:6]

WindDir = list[2][0:3]
if WindDir == "VRB":
    WindDir = "Variable"
elif WindDir == "CLM":
    WindDir = "Calm"
else:
    WindDirDeg = WindDir + "°" #u'\u00b0'
    WindDirection = int(WindDir)
    WindDirComp = Degree(WindDir)

WindSpeed = int(list[2][3:5])
if list[2][5] == "K":
    WindMeasurement = "Knots"
    WindMPH = round(WindSpeed * 1.15078)
elif list[2][5] == "M":
    WindMeasurement = "Meters per Second"
    WindMPH = round(WindSpeed * 2.23694)

Visibility = list[3][:-2]

#Weather Types
if list[4][0:1] == "-":
    Weather1 = "Light"
elif list[4][0:1] == "+":
    Weather1 = "Heavy"
elif list[4][0:2] == "VC":
    Weather1 = "In the vicinity"
elif list[4][0:2] == "MI":
    Weather1 = "Shallow"
elif list[4][0:2] == "PR":
    Weather1 = "Partial"
elif list[4][0:2] == "BC":
    Weather1 = "Patches"
elif list[4][0:2] == "DR":
    Weather1 = "Low drifting"
elif list[4][0:2] == "BL":
    Weather1 = "Blowing"
elif list[4][0:2] == "SH":
    Weather1 = "Showers"
elif list[4][0:2] == "TS":
    Weather1 = "Thunderstorms"
elif list[4][0:2] == "FZ":
    Weather1 = "Freezing"
elif list[4][0:2] == "RA":
    Weather1 = "Rain"
elif list[4][0:2] == "DZ":
    Weather1 = "Drizzle"
elif list[4][0:2] == "SN":
    Weather1 = "Snow"
elif list[4][0:2] == "SG":
    Weather1 = "Snow Grains"
elif list[4][0:2] == "IC":
    Weather1 = "Ice Crystals"
elif list[4][0:2] == "PL":
    Weather1 = "Ice Pellets"
elif list[4][0:2] == "GR":
    Weather1 = "Hail"
elif list[4][0:2] == "GS":
    Weather1 = "Small Hail"
elif list[4][0:2] == "UP":
    Weather1 = "Unknown Precipitation"
elif list[4][0:2] == "FG":
    Weather1 = "Fog"
elif list[4][0:2] == "VA":
    Weather1 = "Volcanic Ash"
elif list[4][0:2] == "BR":
    Weather1 = "Broken Clouds"
elif list[4][0:2] == "HZ":
    Weather1 = "Haze"
elif list[4][0:2] == "DU":
    Weather1 = "Widespread Dust"
elif list[4][0:2] == "FU":
    Weather1 = "Smoke"
elif list[4][0:2] == "SA":
    Weather1 = "Sand"
elif list[4][0:2] == "PY":
    Weather1 = "Spray"
elif list[4][0:2] == "SQ":
    Weather1 = "Squalls"
elif list[4][0:2] == "PO":
    Weather1 = "Dust or Sand Whirls"
elif list[4][0:2] == "DS":
    Weather1 = "Duststorm"
elif list[4][0:2] == "SS":
    Weather1 = "Sandstorm"
elif list[4][0:2] == "FC":
    Weather1 = "Funnel Cloud"
elif list[4][0:3] == "CLR":
    Weather1 = "Clear"
else:
    Weather1 = "Unknown Weather"

print("Airport: " + Airport)
print("Day of Month is: " + Day + "th")
print("Time of Reading: " + Hour + ":" + Minute + " GMT")
print("Wind Direction: " + WindDirDeg)
print("                " + WindDirComp)
print("Wind Speed: " + str(WindSpeed) + " " + WindMeasurement)
print("            " + str(WindMPH) + " Miles per Hour")
print("Visibility: " + Visibility + " Miles")
print("The current weather is " + Weather1)

print("")
print("Press [Enter] to exit.")
input("> ")
