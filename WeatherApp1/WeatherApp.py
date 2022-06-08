from pyowm.owm import OWM
owm = OWM('92172d90c67fba115a78035876416577')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('New York')  # the observation object is a box containing a weather object
weather = observation.weather
weather.status           # short version of status (eg. 'Rain')
 # detailed version of status (eg. 'light rain')
print(weather.detailed_status)