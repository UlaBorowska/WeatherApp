import tkinter as tk 
import requests

height= 500
width =600


def format_response(weather):
	try:
		name = (weather['name'])
		desc = (weather['weather'][0]['description'])
		temp = (weather['main']['temp'])

		final_str = 'City %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'
	return final_str


def get_weather(city):
	weather_key = 'ecb897635400d8f6027bec4272889994'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key,'q': city, 'units': 'metric' }
	response = requests.get(url, params= params)
	weather = response.json()

	label['text'] = format_response(weather)
	
root = tk.Tk()



canvas = tk.Canvas(root, height=height, width=width).pack()

background = tk.PhotoImage(file='land.png')
background_label = tk.Label(root, image= background).place(x=0,y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Calibri', 10))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='check the weather!',font=('Calibri', 10), command=lambda:get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Calibri', 15), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()