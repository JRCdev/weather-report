from geopy.geocoders import Nominatim
from geopy import distance
import os, re, requests

maps = {
"ALASKA":  (65.57, -151.71) ,
"CENTGRLAKES":  (42, -84.75) ,
"GUAM":  (13.46, 144.75) ,
"HAWAII":  (21.17 , -157.120) ,
"NORTHEAST":  (42.4 , -72.84) ,
"NORTHROCKIES":  (43, -108.4) ,
"PACNORTHWEST":  (43, -118) ,
"PACSOUTHWEST":  (35.25, -119.67) ,
"SOUTHEAST":  (30.6, -82.6) ,
"SOUTHMISSVLY":  (32.26, -89.5) ,
"SOUTHPLAINS":  (31.55, -99.7) ,
"SOUTHROCKIES":  (33.9 , -110.11) ,
"UPPERMISSVLY":  (42.8,-96.2) ,
"TJUA":  (18, -65.9 )
}

city = input("Please enter the US city you want a forecast for: ")
geolocator = Nominatim(user_agent="weather-report-user")
location = geolocator.geocode(city)
weathersite = "https://forecast.weather.gov/MapClick.php?lat={}&lon={}&unit=0&lg=english&FcstType=text&TextType=1".format(location.latitude, location.longitude)
searchpage = requests.get(weathersite)
days = re.findall(r"<b>.*<br>\n<br>", searchpage.text)
warnings = re.findall(r"<span class=\"warn\">[\D]*</span>", searchpage.text)

if len(warnings) > 0:
    print("\n\t!!!Warnings!!!\n")
    for warning in warnings:
        print("\t\t \033[1;31m ", warning[18:-7], " \033[0m")
    print("\nPlease check https://weather.gov for more information!\n\n")

for day in days:
    print(day[3:day.find(" </b>")-1], "|", day[day.find(" </b>")+5:-10], "\n")

mindist = 3000
minnm = "CONUS-LARGE"
for mapnm in maps:
    dist = distance.distance((location.latitude, location.longitude), maps[mapnm]).miles
    if dist < mindist:
        mindist = dist
        minnm = mapnm

site = "https://radar.weather.gov/ridge/lite/{}_loop.gif".format(minnm)
print("Closest matching map is " + minnm)
print("Available at", site)
os.system("mpv --loop-file {}".format(site))
