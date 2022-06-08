from tkinter import *
from configparser import ConfigParser
import messagebox
import requests
from PIL import Image, ImageTk
response = requests.request('GET', 'http://www.alandmoore.com')


url = 'http://api.openweathermap.org/data/2.5/weather?&q={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']



def get_weather(city):
	result = requests.get(url.format(city, api_key))
	if result:
		json = result.json()
		#(City, Country, temp_celcius, temp_fahreinheit, icon, weather)
		city = json['name']
		country = json['sys']['country']
		temp_kelvin = json['main']['temp']
		temp_celcius = temp_kelvin - 273.15
		temp_fahrenheit = (temp_kelvin - 273.15)* 9 / 5 + 32
		icon = json['weather'][0]['icon']
		weather = json['weather'][0]['main']
		final = (city, country, temp_celcius, temp_fahrenheit, icon, weather)
		return final
	else:
		return None


#print(get_weather('London'))







app = Tk()
app.title('Weather App')
app.geometry("700x350")

#city_text = StringVar()
#city_entry = Entry(app, textvariable=city_text)
city_entry = Entry(app)

city_entry.pack()

def search():
	city = city_entry.get()
	weather = get_weather(city)
	#print(weather)
	if  weather:
		location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
		#image['bitmap'] = '02d.png'#'{}.png'.format(weather[4])
		#image1 = '{}.png'.format(weather[4])
		#img2=ImageTk.PhotoImage(Image.open(image1))
		#image.configure(image=img2)
		#image.image=img2
		temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
		weather_lbl['text'] = weather[5]
	else:
		messagebox.showerror('Error','Cannot find city {}'.format(city))

search_btn = Button(app, text = 'Search Weather', width = 12, command= search)
search_btn.pack()

location_lbl = Label(app, text = 'Location', font =( 'bold', 20))
location_lbl.pack()

image = Label(app, bitmap='')


temp_lbl = Label(app, text= 'Temperature')
temp_lbl.pack()

weather_lbl = Label(app, text = 'weather')
weather_lbl.pack()


app.mainloop()