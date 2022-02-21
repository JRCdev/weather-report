# weather-report
A python CLI that pulls up a 7-day US forecast and an appropriate radar from weather.gov

![Couldn't resist](https://static.wikia.nocookie.net/jjba/images/3/38/Weather_Report.png/revision/latest/scale-to-width-down/522?cb=20191202033913)

Requirements:

`mpv` is added to your `PATH`

The following python packages: `geopy`, `re`, `requests`

How it works: 
 1. The geopy package gets the latitude and longitude of your city. That part works globally! Even with landmark names and addresses.
 2. With that we can look up the 7-day forecast directly, which'll be rerouted to whatever station's closest
 3. Special mark is made for warnings, which should appear in red in most terminals
 4. Trickier: There are a dozen or so big regional maps, I had to make a lookup table to find the rough center of each
 5. The same Geopy package then finds out which one is closest to the given location
 6. mpv is then invoked to loop the GIF that displays that region's latest 
