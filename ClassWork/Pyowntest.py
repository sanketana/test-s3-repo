from pyowm.owm import OWM
owm = OWM('3bbec63ba1186808140911815f9a0d04')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Bangalore, IN')  # the observation object is a box containing a weather object
weather = observation.weather
weather.status           # short version of status (eg. 'Rain')
print(weather)  # detailed version of status (eg. 'light rain')
