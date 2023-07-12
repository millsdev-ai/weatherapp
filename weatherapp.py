import tkinter as tk
import requests
import time

# Function to get the weather data from the API
def getWeather(canvas):
    # Get the city name from the text field
    city = textField.get()

    # Get the weather data from the API
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"

    # Send a request to the API and get the JSON data
    json_data = requests.get(api).json()

    # Get the weather data from the JSON data
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 0))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 0))

    # Create the final string for showing the weather data
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


# Create the canvas for the GUI
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")
c = ("poppins", 20, "bold")

# Create the label for showing the weather data
label1 = tk.Label(canvas, text=" Enter a City :" , font = c)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

# Create the text field for entering location
textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

# Create the button for fetching weather data
button = tk.Button(canvas, text="Get Weather", font=f, command=getWeather)
button.pack(pady=10)

# Run the tkinter event loop
canvas.mainloop()
