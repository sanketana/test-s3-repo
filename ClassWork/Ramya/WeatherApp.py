import tkinter as tk
from pyowm.owm import OWM



window = tk.Tk()
window.title("Ramya's Weather App")

ent_city = tk.Entry(window)
ent_city.grid(row=1, column=1)

lbl_max_temp_label = tk.Label(window, text="Maximum Temperature")
lbl_max_temp_label.grid(row=2, column=1)

lbl_max_temp = tk.Label(window, text="")
lbl_max_temp.grid(row=2, column=2)


lbl_curr_weather_label = tk.Label(window, text="Current Weather")
lbl_curr_weather_label.grid(row=3, column=1)

lbl_curr_weather = tk.Label(window, text="")
lbl_curr_weather.grid(row=3, column=2)


def getWeather():
	owm = OWM('92172d90c67fba115a78035876416577')
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(ent_city.get())  # the observation object is a box containing a weather object
	weather = observation.weather
	weather.status           # short version of status (eg. 'Rain')
	weather.detailed_status  # detailed version of status (eg. 'light rain')
	lbl_curr_weather.configure(text = weather.detailed_status )



btn_submit = tk.Button(window, text="Search", command=getWeather)
btn_submit.grid(row=1, column=2)




window.mainloop()