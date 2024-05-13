#all lines of work from line 2 - 25 are mine or done in class
import requests
from tkinter import *
from tkinter.ttk import *
from time import strftime
from ttkthemes import ThemedTk

root = ThemedTk(theme="black")  # Change the theme here
root.configure(background='black') #changes theme color


# Remove window controls (close, minimize, expand)
root.overrideredirect(True)

root.title('Desktop Widget') #titles it

def display_time():
    time_string = strftime('%I:%M %p')  # Removed seconds from the time format
    time_label.config(text=time_string) # updates lines on GUI
    time_label.after(1000, display_time) # updates them after 1 second

def display_date():
    date_string = strftime('%A, %B %d, %Y')
    date_label.config(text=date_string) # updates lines on GUI
    date_label.after(1000, display_date) # updates them after 1 second
#all code from line 26 - 39 was taken from the internet and fixed by me, for example, i made the celsuis conversion
def display_weather():
    api_key = "2006a8f5129dd2655f8213200f0281e2" #api key from openweathermap.org
    city_id = "5392171"  # City ID for San Jose, California
    url = f"http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200: # IF function gathers data descriptions and displays them on GUI
        weather_desc = data["weather"][0]["description"].capitalize()
        temperature_celsius = data["main"]["temp"]
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32  # Converts Celsius to Fahrenheit
        weather_label.config(text=f"San Jose, {weather_desc}, Temperature: {temperature_fahrenheit:.2f}°F")
    else:
        weather_label.config(text="Weather data unavailable") #shows not available if API key is wrong or not working
    root.after(60000, display_weather)  # Fetch weather data every minute
# all code here on is my own
# Labels for date, time, and weather
# tried making background transparent but does not work with tkinter
time_label = Label(root, font=('Lato', 90), background='systemTransparent', foreground='white')
time_label.pack(anchor='center')
display_time()
# Labels for date, time, and weather
date_label = Label(root, font=('Lato', 24), background='systemTransparent', foreground='white')
date_label.pack(anchor='center')
display_date()
# Labels for date, time, and weather
weather_label = Label(root, font=('Lato', 18), background='systemTransparent', foreground='white')
weather_label.pack(anchor='center')
display_weather()

root.mainloop()
# References https://home.openweathermap.org/api_keys
#https://www.youtube.com/watch?v=baWzHKfrvqw
#https://ttkthemes.readthedocs.io/en/latest/themes.html
#https://www.instructables.com/Get-Weather-Data-Using-Python-and-Openweather-API/