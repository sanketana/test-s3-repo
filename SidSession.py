#use case - find the current weather conditions at Mumbai, Singapor
#use case - forecase for next 1 week
from pyowm.owm import OWM
owm = OWM('66e7ab871932bb6c552d740ed870a780')
mgr = owm.weather_manager()
city = input('City: ')
observation = mgr.weather_at_place(city)  # the observation object is a box containing a weather object
weather = observation.weather
print(weather.detailed_status)


#weather.status           # short version of status (eg. 'Rain')
#weather.detailed_status  # detailed version of status (eg. 'light rain')

